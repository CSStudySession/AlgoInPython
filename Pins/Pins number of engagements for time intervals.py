'''
https://leetcode.com/company/pinterest/discuss/5542874/Pinterest-Screening-Interview-or-MLE-July-2024

"engagement" is a very important metric for Pinterest. 
Given an array of start times and end times for pins, write an algorithm that returns number of engagements for time intervals.
For example, input: [[0,5],[1,2],[3,7]]
output:
[0,1] -> 1
[1,2] -> 2
[2,3] -> 1
[3,5] -> 2
[5,7] -> 1

思路：
需要计算每个时间间隔内有多少个活动在进行。
可以将每个开始时间和结束时间标记为事件，然后遍历这些事件来计算每个时间段的参与度。

1. 提取时间点:将所有的开始时间和结束时间提取出来 排序后得到所有的关键时间点
2. 计算每个区间的参与度:遍历时间点 计算每个时间区间内有多少个活动正在进行
time: O(nlogn)
space: O(n)
'''
from typing import List

def calculate_engagement(intervals:List[List[int]]) -> List[tuple]:
    if not intervals:
        return []
    # 提取所有的开始时间和结束时间 并标记它们是开始还是结束
    events = []
    for start, end in intervals:
        events.append((start, 'start'))
        events.append((end, 'end'))
    # 按时间点进行排序
    events.sort()
    cur_egmt = 0  # 当前的参与度
    result = []   # list of tuple:(interval_start, interval_end, egmt_num)
    # 遍历所有的时间点
    for i in range(len(events) - 1):
        time, event_type = events[i]
        next_time = events[i + 1][0]
        
        if event_type == 'start':
            cur_egmt += 1
        else:
            cur_egmt -= 1
        
        # 如果当前时间与下一个时间不相同，则记录该时间段的参与度: 只在实际的时间区间发生变化时记录参与度
        # 排序后 相邻的事件可能会有相同的时间点 比如在两个活动同时结束的情况
        if time != next_time:
            result.append((time, next_time, cur_egmt))
    return result

# 测试
intervals = [[0,5],[1,2],[3,7]]
engagements = calculate_engagement(intervals)
for item in engagements:
    print(f"[{item[0]},{item[1]}] -> {item[2]}")