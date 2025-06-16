'''
给定直播的历史数据 从历史记录中 求某一时刻最多有多少个直播同时进行
输入:一组直播元数据 每条记录格式为
[直播ID, 直播时长, 观看人数, 开始时间, 结束时间]
(仅需使用[开始时间, 结束时间]来解决本题）
输出:一个整数 表示任意时刻最多有多少个直播在进行中
Clarification
时间单位与格式: 时间统一为从epoch开始的秒数(例如用time.time()得到的值)
时间只需保持一致格式 精确度到秒
只考虑已完成的直播:不考虑正在进行但尚未结束的直播。
每个直播都有有效的开始与结束。
同一时间开始或结束怎么办?若直播A结束时间=B开始时间 算作同时进行 (这个点要问清楚 下面堆的pop操作靠它)
最小直播时长? 直播至少持续1单位时间(即start_time ≠ end_time)
'''

'''
解法1: sort + sweepline
每个直播 [start, end) 看作两个事件:
+1 表示 start(开始时刻记为直播进入)
-1 表示 end(结束时刻记为直播退出)
“若 A.end == B.start 算作同时进行”, 因此:
start 是直播进入点 +1
end 是直播退出点，但仍算“正在进行” 所以在end + 1时记作 -1(即直播在 end 秒仍然存在)
遍历新的events数组 更新一个max_live值即可.
T(nlogn) S(n)
'''
def max_concurrent_streams(metadata_list):
    if not metadata_list:
        return 0
    events = []
    for data in metadata_list:
        start, end = data[3], data[4]
        events.append((start, 1))        # 直播开始
        events.append((end + 1, -1))     # 直播在 end 秒仍然存在，end+1 再退出
    # 排序按时间点，时间相同的先加后减（默认排序满足）
    events.sort()
    max_live = 0
    cur_live = 0
    for _, delta in events:
        cur_live += delta
        max_live = max(max_live, cur_live)
    return max_live


'''
解法2: sort + min-heap
- 将所有直播按照start_time升序排序
- 使用一个min-heap来存放“正在进行的直播”的end_time
- 遍历所有start_time
  - 若堆顶的最早end_time ≤ 当前start_time 则说明对应直播已结束, pop出
  - 当前直播加入堆中；
  - 用堆的大小更新最大并发直播数
返回整个过程中堆的最大大小
T(nlogn) S(n)
'''
import heapq
def max_concurrent_streams(metadata_list):
    if not metadata_list:
        return 0
    # 提取并排序所有直播的开始和结束时间
    time_pairs = sorted([(data[3], data[4]) for data in metadata_list])  # 按开始时间排序
    ongoing_end_heap = []  # 小顶堆存储正在进行直播的结束时间
    max_cnt = 0

    for start_time, end_time in time_pairs:
        # 移除所有已结束的直播
        while ongoing_end_heap and ongoing_end_heap[0] < start_time:
            heapq.heappop(ongoing_end_heap)
        # 当前直播加入堆中
        heapq.heappush(ongoing_end_heap, end_time)
        # 更新最大并发数
        max_cnt = max(max_cnt, len(ongoing_end_heap))
    return max_cnt

'''
解法3: two min-heaps
- 拆分出所有start_times与end_times 分别构建两个小顶堆
- 用两个指针遍历两个堆
  - 如果最早的 start_time ≤ 当前最早的 end_time 说明有直播开始 count+1
  - 否则 结束时间先到了 说明有直播结束 count-1
  - 每次更新最大并发数
返回最大并发数
T(nlogn) S(n)
'''
def max_concurrent_streams_dual_heap(metadata_list):
    if not metadata_list:
        return 0
    start_heap = [data[3] for data in metadata_list]
    end_heap = [data[4] for data in metadata_list]
    heapq.heapify(start_heap)
    heapq.heapify(end_heap)

    cur_cnt = 0
    max_cnt = 0

    while start_heap:
        if start_heap[0] <= end_heap[0]:
            heapq.heappop(start_heap)
            cur_cnt += 1
            max_cnt = max(max_cnt, cur_cnt)
        else:
            heapq.heappop(end_heap)
            cur_cnt -= 1
    return max_cnt