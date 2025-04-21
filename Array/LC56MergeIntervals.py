from typing import List
'''
Time o(nlogn) for sorting, Space o(1)
if current interval does not overlap with the previous: append previous one to result.
else, if overlap: update previous ending to be max(current, previous)
'''
def merge(intervals: List[List[int]]) -> List[List[int]]:
    ret = []
    intervals = sorted(intervals) # sorted on first element of inner list
    prev_left, prev_right = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > prev_right:
            ret.append([prev_left, prev_right])
            prev_left, prev_right = intervals[i][0], intervals[i][1]
        else:
            prev_right = max(prev_right, intervals[i][1]) # 注意这里只更新right 不能append. 后面可能还有重叠的intervals
    ret.append([prev_left, prev_right]) # last interval needs to process outside of for loop
    return ret