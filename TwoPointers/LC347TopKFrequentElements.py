import collections
from typing import List

'''
solution 1: 维护size为k的min-heap. 堆上的元素为tuple:(cnt, num). python heap默认按照first key排序.
通过Counter获得(num, cnt) 然后遍历counter 构造min-heap.
'''
def topKFrequent(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    
    import heapq
    heap = []
    counter = collections.Counter(nums)
    for num, cnt in counter.items(): # 注意.items()是(num, cnt) 顺序别反了 
        if len(heap) < k:
            heapq.heappush(heap, (cnt, num))
        elif cnt > heap[0][0]: # 优化 只有当cnt>堆顶元素的cnt时 才可能是解 否则不用入堆
            heapq.heappushpop(heap, (cnt, num))
    
    ret = []
    while heap:
        ret.append(heapq.heappop(heap)[1]) # 注意heap pop的语法
    return ret    # 如果需要按cnt从大到小 就reverse一下


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if not nums:
        return []
    counter = collections.Counter(nums)
    keys = list(counter.keys())
    partition(counter, keys, 0, len(keys) - 1, k)
    return keys[:k] # k取不到 [0...k-1]


def partition(counter, keys, start, end, k):
    while start < end:
        left, right = start, end  # [start, left) (right, end] 两个区间
        pivot = counter[keys[(start + end) // 2]] # 注意pivot是counter对应的值
        while left <= right:
            while left <= right and counter[keys[left]] > pivot: # 这里与pivot相比时不能取到=
                left += 1
            while left <= right and counter[keys[right]] < pivot:
                right -= 1
            if left <= right: # 注意要交换完元素 l/r需各走一步
                keys[left], keys[right] = keys[right], keys[left]
                left += 1
                right -= 1
        if k >= left:
            start = left
        elif k <= right:
            end = right
        else: return # 一定要return

# 变形:输入是linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def topKFrequent(head: 'ListNode', k: int) -> list:
    # Step 1: Count the frequency of each element in the linked list
    # 用linked list计算counter
    frequency = collections.defaultdict(int)
    current = head
    while current:
        frequency[current.val] += 1
        current = current.next
    # Step 2: Use a min-heap to keep track of the top k elements
    min_heap = []
    import heapq
    for num, freq in frequency.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        elif freq > min_heap[0][0]:
            heapq.heappushpop(min_heap, (freq, num))
    # Step 3: Extract the elements from the heap
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    return result