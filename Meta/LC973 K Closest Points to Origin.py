from typing import List
import heapq
# 解法1: max-heap. T(nlog(k)) S(k)
def kClosest_v1(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for i in range(len(points)):
        # negate the distance to simulate max heap(默认小根堆)
        dist = -calc_dist(points[i])
        # fill the heap with the first k elements of points
        if len(heap) < k:
            heapq.heappush(heap, (dist, i))
        elif dist > heap[0][0]:
            # If this point is closer than the kth farthest,
            # discard the farthest point and add this one
            # 注意这个if算是一个常数级别的优化 避免多余的heap push/pop Meta followup可能问
            heapq.heappushpop(heap, (dist, i))
    
    # Return all points stored in the max heap
    ret = []
    for _, idx in heap:
        ret.append(points[idx]) # 注意这里是idx 别写成i
    return ret
# Calculate and return the squared Euclidean distance.
def calc_dist(self, point: List[int]) -> int: # 不需要开根号
    return point[0] ** 2 + point[1] ** 2 #  算平方用'**'

# 解法2: quick selection
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    quick_selection(points, 0, len(points) - 1, k)
    return points[:k]

def quick_selection(points: List[List[int]], start: int, end: int, k: int):
    while start <= end:
        left, right = start, end
        pivot = calc_dist(points[(start + end) // 2])
        while left <= right:
            while left <= right and calc_dist(points[left]) < pivot: # 这里与pivot相比时不能取到=
                left += 1
            while left <= right and calc_dist(points[right]) > pivot:
                right -= 1
            if left <= right: # 注意交换完 指针也要更新
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1

        if k <= right:
            end = right
        elif k >= left:
            start = left
        else: return # 注意一定要return. k落在等于pivot区间里 直接返回 否则死循环

def calc_dist(self, point) -> int:
    return point[0] ** 2 + point[1] ** 2