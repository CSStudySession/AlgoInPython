import collections, heapq
'''
1. After we build our window, the length of window will ALWAYS be the same 
(now we will keep the length of valid elements in max_heap and min_heap the same too)

2. Based on this, when we slide our window, the balance variable can be equal to 0, 2 or -2. 
It will NEVER be -1 or 1.
Examples:
0 -> when we remove an element from max_heap and then add a new one back to max_heap 
(or the same for min_heap)
-2 -> when we remove an element from max_heap and then add a new one to min_heap 
(max_heap will have two less elements)
2 -> when we remove an element from min_heap and then add a new one to max_heap 
(min_heap will have two less elements)
3. Based on this - it is enough for us to move 1 element from one heap to another 
when the balance variable is equal to 2 or -2
T(n*log(k))  S(k)
'''
def medianSlidingWindow(nums: list[int], k: int) -> list[float]:
    min_heap, max_heap = [], []
    ret = []
    to_delete = collections.defaultdict(int)

    for i in range(k):
        heapq.heappush(max_heap, -nums[i]) # 先进大根堆 再pop到小根堆
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap): # 保持大跟堆size >= 小根堆
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    median = find_median(max_heap, min_heap, k)
    ret.append(median)

    for i in range(k, len(nums)):
        prev_num = nums[i - k]
        to_delete[prev_num] += 1

        balance = -1 if prev_num <= median else 1
        
        if nums[i] <= median:
            balance += 1
            heapq.heappush(max_heap, -nums[i])
        else:
            balance -= 1
            heapq.heappush(min_heap, nums[i])
        
        if balance < 0:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif balance > 0:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # 要先清理大根堆 因为会有重复元素 当大根堆和小根堆都有待删除的元素时
        # 因为大根堆的元素多 所以先清理掉大根堆后 to_delete[x]可能不需要在小根堆清理了
        while max_heap and to_delete[-max_heap[0]] > 0: 
            to_delete[-max_heap[0]] -= 1
            heapq.heappop(max_heap)

        while min_heap and to_delete[min_heap[0]] > 0:
            to_delete[min_heap[0]] -= 1
            heapq.heappop(min_heap)
    
        median = find_median(max_heap, min_heap, k)
        ret.append(median)
    return ret

def find_median(max_heap, min_heap, k):
    if k % 2 == 1:
        return -max_heap[0]
    else:
        return (-max_heap[0] + min_heap[0]) / 2