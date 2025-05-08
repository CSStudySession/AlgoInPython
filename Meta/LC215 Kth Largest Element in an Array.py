from typing import List
'''
解法1: min heap.注意入堆操作时 有个优化!
T: O(n*lg(k))  S:O(k)
'''
def findKthLargest0(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    heap = []
    import heapq # 默认是min heap
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]: # 优化点!只有在当前num>堆顶时 才进行pushpop操作
                            # 如果num<=堆顶 则num一定不会是第k大(堆顶比num更有可能是)
            heapq.heappushpop(heap, num)
    return heap[0] # 堆顶元素是k个在堆里元素中 最小的 -> 第k大

'''
解法2: quick select
随意选一个pivot number, move all smaller to left of pivot, all larger to right of pivot.
T: avg O(n) worst O(n^2)  S: O(h) due to recursion call.
'''
def findKthLargest1(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    k = len(nums) - k
    return quickSelect(nums, k, 0, len(nums) - 1)

def quickSelect(nums, k, start, end) -> int:
    pivot = nums[start]
    left, right = start, end  # 要重新assign pointer, 因为需要left right不断移动
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    # 结束的时候left在右 right在左[start, right, left, end]
    if k >= left:
        quickSelect(nums, k, left, end)
    if k <= right:
        quickSelect(nums, k, start, right)
    return nums[k]

'''
variant: return the kth + 1 largest num.
解法: min heap. 注意由于k要+1 有各种corner cases! ask clarification questions:
1. range of k? what if k+1>len(nums) can k <= 0? 2. range of length if nums? 
T: O(n*lg(k))  S:O(k)
'''
def find_K_plus_one_largest(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    if k + 1 > len(nums):
        return 0
    k = k + 1 # 用k+1替换原来的k
    heap = []
    import heapq # 默认是min heap
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]: # 优化点!只有在当前num>堆顶时 才进行pushpop操作
                            # 如果num<=堆顶 则num一定不会是第k大(堆顶比num更有可能是)
            heapq.heappushpop(heap, num)
    return heap[0] # 堆顶元素是k个在堆里元素中 最小的 -> 第k大

'''
variant2: return kth smallest
思路:用max-heap保存当前k个最小值. 堆顶元素是最大堆中 最小的负数
'''
def find_Kth_smallest(nums: List[int], k: int) -> int:
    if not nums:
        return 0
    heap = []
    import heapq # 默认是min heap 取负数入堆变大根堆
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif num < -heap[0]: # 当前元素比大根堆堆顶元素小 可能是答案 应该入堆
            heapq.heappushpop(heap, -num)
    return -heap[0]  # 堆顶是第k小 (最大堆中最小的负数)