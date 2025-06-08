from collections import defaultdict
'''
构建一个骚扰电话数据库，输入是两个数据表（带噪声），要求完成 fuzzy join 匹配，
并统计每个被标记为骚扰的主叫号码的举报次数。

input
Table 1 (telecom call logs):
记录电话通话信息：
[src_phone_num, dst_phone_num, start_time]
# 主叫号码，被叫号码，开始时间（字符串）
Table 2 (smartphone spam reports)
记录用户标记骚扰的记录：
[dst_phone_num, start_time, is_spam]
# 被叫号码，开始时间，是否标记为骚扰
注意:
- T1 和 T2 没有共享ID 无法直接 join。
- timestamp允许最多2秒误差进行 fuzzy join
- T1、T2按时间有序 时间单位为整数秒
- you may assume you have the following fuctions that convert timestamps to unix time:
ts_to_unix_time('2023-06-01 12:01:01') -> 123434235.0
unix_time_sec_to_ts(12312432.0) -> '2023-06-01 12:04:06'

output 一个统计结果的列表:
[src_phone_num, dst_phone_num, report_count]
表示这个主叫号码被这个被叫号码举报为spam的次数. 只输出report_count > 0的记录
思路：
预处理 T2 为字典结构 key 是 (dst_phone_num, timestamp)。
遍历 T1 中每一行 即每一通电话
  - 把 timestamp 转为 unix 时间戳。
  - 枚举该时间戳在 ±2 秒范围内的所有可能 timestamp
  - 在 T2 中查找是否有 is_spam=True 的匹配。
    - 若找到，计数器 +1。
最终根据计数器构造结果。
T(len(table1) + len(table2))  S(len(table1) + len(table2))
'''
from typing import List, Dict, Tuple, Optional
import datetime, time

# 时间戳转为 unix 秒数 可以假设given
def timestamp_to_unix_time_secs(timestamp: str) -> float:
    return time.mktime(datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").timetuple())

# unix 秒数转为时间戳 可以假设given
def unix_time_secs_to_timestamp(unix_time_secs: int) -> str:
    return datetime.datetime.fromtimestamp(unix_time_secs).strftime("%Y-%m-%d %H:%M:%S")

# 匹配 T1 的某一条记录 row_t1，找到 T2 中最合适的 row
def find_matching_row(row_t1: List, map_t2: Dict[Tuple[str, str], List], diff_secs: int = 2) -> Optional[List]:
    dst_phone_num = row_t1[1]
    timestamp_t1 = row_t1[2]
    unix_secs_t1 = int(timestamp_to_unix_time_secs(timestamp_t1))

    # 枚举 [-2, 2] 秒误差内的时间戳 虽然是循环 但是次数固定 T(1)
    for delta in range(-diff_secs, diff_secs + 1):
        cur_ts = unix_time_secs_to_timestamp(unix_secs_t1 + delta)
        key = (dst_phone_num, cur_ts)
        if key in map_t2 and map_t2[key][2]:  # is_spam为True
            return map_t2[key]  # 只要能match到就可以返回了
    return None # match不到 return None

# main function
def generate_spam_number_database(table1: List[List], table2: List[List]) -> List[List]:
    # 构建 T2 的字典索引 key:(dst_phone_num, timestamp), value: row的reference
    map_t2 = {}
    for row in table2:
        key = (row[0], row[1])
        map_t2[key] = row
    # 统计 spam
    spam_to_cnt = defaultdict(int)
    for row in table1:
        matched_row = find_matching_row(row, map_t2)
        if matched_row:
            src, dst = row[0], row[1]
            spam_to_cnt[(src, dst)] += 1
    # 输出结果
    ret = []
    for (src, dst), cnt in spam_to_cnt.items():
        ret.append([src, dst, cnt])
    return ret

'''
followup: 如果时间戳不再是整数（即是 float 秒，例如带毫秒）怎么办？(不用写code 下面的code可以参考)
HashMap 就不适用了，因为 key 不能是连续 float 值。
改为：对 T2 做 binary search 允许在范围[t-2s, t+2s]内搜索。
时间复杂度会变为:
O(len(T1) * log(len(T2)))
思路:
对 rows_table2 预处理成dst_phone_num → 所有记录（按 timestamp 升序）
每次匹配时，对于 (dst, time)，从对应列表中二分出所有在 [t-2, t+2] 区间的记录
检查这些记录中是否有 is_spam=True 选出最早的那条即可
'''
# 构建每个 dst 的 T2 记录（按时间排序）
def build_index(rows_table2: List[List]) -> Dict[str, List[Tuple[float, List]]]:
    index = defaultdict(list)
    for row in rows_table2:
        dst = row[0]
        ts = timestamp_to_unix_time_secs(row[1])
        index[dst].append((ts, row))
    # 对每个 dst 的 list 按时间排序
    for lst in index.values():
        lst.sort()
    return index

# 在 [t-2, t+2] 内二分查找最早的 spam=True 的 T2 行
def binary_search_match(dst: str, t1_time: float, index: Dict[str, List[Tuple[float, List]]], diff_secs: float = 2.0) -> List:
    if dst not in index:
        return None
    candidates = index[dst]
    lo = bisect.bisect_left(candidates, (t1_time - diff_secs, ))
    hi = bisect.bisect_right(candidates, (t1_time + diff_secs, ))

    for i in range(lo, hi):
        if candidates[i][1][2]:  # is_spam=True
            return candidates[i][1]
    return None
# 主函数
def generate_spam_number_database(rows_table1: List[List], rows_table2: List[List]) -> List[List]:
    index = build_index(rows_table2)
    counter = Counter()
    for row in rows_table1:
        src, dst, ts_str = row
        ts = timestamp_to_unix_time_secs(ts_str)
        match = binary_search_match(dst, ts, index)
        if match:
            counter[(src, dst)] += 1
    return [[src, dst, count] for (src, dst), count in counter.items()]
