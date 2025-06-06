'''

'''
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if not intervals: return [newInterval]
    start = newInterval[0]
    if newInterval[0] < intervals[0][0]: # 当前区间比首区间的起点都小
        intervals.insert(0, newInterval) 
    else: # 找最后一个小于等于start的区间起点 返回对应区间index
        index = binarySearch(intervals, start)
        intervals.insert(index + 1, newInterval) # 在它后面插入 
    res = [] # 顺序扫描merge区间
    for i in range(len(intervals)):
        x, y = intervals[i]
        if not res or res[-1][1] < x:
            res.append([x, y])
        else:
            res[-1][1] = max(res[-1][1], y)
    return res
# 找最后一个小于等于target的区间左端点 并返回对应区间下标
def binarySearch(intervals, target):
    left, right = 0, len(intervals) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if intervals[mid][0] <= target:
            left = mid
        else:
            right = mid - 1
    return right

