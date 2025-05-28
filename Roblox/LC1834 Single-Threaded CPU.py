import heapq
''''
思路:sort+heap
- 先给每个任务加上下标 并按到达时间排序
- 用一个小顶堆维护所有已到达但未处理的任务 堆里按照处理时间和下标排序 
  每次先把所有可到达的任务入堆 如果堆为空则快进到下一个任务的到达时间
  堆不为空就取出处理时间最短的任务执行并更新时间 直到所有任务都被处理完
T(nlogn) S(n)
'''
def getOrder(tasks: list[list[int]]) -> list[int]:
    # 需要先按开始时间sort, 但是sort之前需要先记住index
    # 所以把index也加入每个task list里: (start, procTime, index)
    for i, task in enumerate(tasks):
        task.append(i)
    tasks = sorted(tasks, key = lambda x: x[0])
    
    res = []
    time = 0
    heap = []
    i = 0
    while heap or i < len(tasks):
        while i < len(tasks) and time >= tasks[i][0]:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2])) # heap里只需要放procTime, index
            i += 1
        if not heap:
            time = tasks[i][0] # no tasks is processing and CPU idle 
                               # so reset time to be the next task
        else:
            procTime, index = heapq.heappop(heap)
            time += procTime
            res.append(index)
    return res