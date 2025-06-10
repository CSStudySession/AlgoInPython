'''
给出每个用户对某个 Pin 的互动时间区间 [start, end)，统计并输出每个连续时间段中有多少 Pin 正在被互动。
时间粒度为1秒钟 所有时间戳 start, end 都是整数。
输入格式：
input = [
  ["pinA", 0, 5],
  ["pinB", 1, 2],
  ["pinC", 3, 7]
]
输出格式：
[
  [0, 1, 1],
  [1, 2, 2],
  [2, 3, 1],
  [3, 5, 2],
  [5, 7, 1]
]
每个子数组表示 [start_time, end_time, count]：这个时间区间内，有多少个 pin 被互动。
Clarifications(题目中明确说明的约束)
start < end 输入永远有效。
所有时间值都小于60(即只处理1分钟内的时间段)
不用担心内存，数据 fit in memory, 时间粒度为秒(每个 slot 是 1 秒)
思路:
利用 计数数组(sec_cnt)对每一秒记录有多少个Pin在互动。
然后扫一遍，把连续值相同的时间段合并输出。
T(n_t) n is # of records, t is max time range(60s)
S(t) worst 60s
'''
def count_pin_engagement(time_data):
    # 初始化每一秒的计数器（最多60 秒）
    sec_cnt = [0] * 60
    # 遍历每个记录，在对应时间段打点计数
    for _, t_start, t_end in time_data:
        for t in range(t_start, t_end):
            sec_cnt[t] += 1
    # 生成时间段区间输出
    ret = []
    left = 0
    while left < 60:
        right = left
        # 继续向右扩展，直到值发生变化
        while right < 60 and sec_cnt[right] == sec_cnt[left]:
            right += 1 # right停在60 或者 s[r] != s[l]的位置
        if sec_cnt[left] != 0:
            ret.append([left, right, sec_cnt[left]])
        left = right # 更新left为right 给下一次循环用
    return ret

'''
Follow-up 问题（图片中提到）：
1. 移除 start/end 限制(不一定在 0~60)
如果时间不再限制在 0~60 秒 不能用固定数组了 可以改用defaultdict(int)处理稀疏时间戳。
2. 存在重复数据（同一个 pin 重复出现）：
要处理如:
[{"A", "B"}, 0, 5] [{"B", 1, 2}] [{"C", "D"}, 3, 7] 这种情况下, "B"重复出现
示例输出:
[0,3] ⇒ 2    # A + B
[3,5] ⇒ 4    # A + B + C + D
[5,7] ⇒ 2    # C + D

思路:

'''
from collections import defaultdict

def count_engagement_with_dedup(time_data):
    # 使用 defaultdict 统计每秒有多少个 pin 被互动
    time_counter = defaultdict(int)
    seen = set()  # 防止重复：记录 (pin_name, time) 是否已经处理过
    
    for pin_name, t_start, t_end in time_data:
        for t in range(t_start, t_end):
            key = (pin_name, t)
            if key not in seen:
                time_counter[t] += 1
                seen.add(key)

    # 对所有有计数的时间点进行排序
    result = []
    times = sorted(time_counter.keys())
    i = 0
    # 将连续时间点中 计数值相同的时间段合并为一个[start, end, count]区间
    while i < len(times):
        start = times[i]
        count = time_counter[start]
        end = start + 1
        # 合并连续且值相同的时间段. times[i + 1] == end -> 必须是连续秒
        # cnt[end] == cnt 值不变. 加上i+1不能越界 三个条件同时满足 才能合并
        while i + 1 < len(times) and times[i + 1] == end and time_counter[end] == count:
            end += 1
            i += 1
        result.append([start, end, count])
        i += 1
    return result

# test
input_data = [
    ["pinA", 0, 5],
    ["pinB", 0, 5],  # 与 pinA 重叠
    ["pinB", 1, 2],  # pinB 在 1 秒重复
    ["pinC", 3, 7],
    ["pinD", 3, 7]
]
print(count_engagement_with_dedup(input_data))