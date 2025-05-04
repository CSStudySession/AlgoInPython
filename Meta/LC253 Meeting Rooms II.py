'''
1. 将每个会议的开始和结束时间拆成两个事件 开始时间标记为+1 结束时间标记为-1
 -- [0, 30] 变成 (0, +1)会议开始  (30, -1)会议结束
2 把所有事件按照时间排序.如果同一时刻有开始和结束 先处理结束事件-1 这样不会有额外的房间需求
 -- python sort在第二key时 自动会把(x, -1)放前面
3. 遍历sort过的事件集合 每遇到一个事件就调整room += +1 或 -1,过程中维护max_room
T(nlogn) S(n)
'''
def minMeetingRooms(intervals: list[list[int]]) -> int:
    ts = []
    for interval in intervals:
        ts.append((interval[0], 1))
        ts.append((interval[1], -1))
    ts.sort() # sort()是in-place sorted(list)是创建一个新list
    max_room = 0
    cnt = 0
    for i in range(len(ts)):
        cnt += ts[i][1]
        max_room = max(max_room, cnt)
    return max_room