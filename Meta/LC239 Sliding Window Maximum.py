import collections
'''
维护一个monotolic queue存index 对应元素单调递减.保证头元素是最大的 尾部每见到一个更大的 就把小的pop
单调队列维护顺序: 
1.检查队列元素是否满足在窗口内
2.检测队尾元素与当前元素的大小关系 如果与单调性相反 一直pop直到当前元素可以入队
3.当前元素入堆. 队列长度如果满足条件 队头元素放入结果集.
T(n) S(n)
'''
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    ret = []
    queue = collections.deque()
    for i in range(len(nums)):
        if queue and queue[0] < i - k + 1:
            queue.popleft()
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
        if i >= k - 1:
            ret.append(nums[queue[0]])
    return ret