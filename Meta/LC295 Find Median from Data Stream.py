import heapq
'''
思路:max/min双堆
|<---------->|<------->|
    left        right
left部分和right部分 分别用maxHeap和minHeap维护 每次查找 只找相应的堆顶即可
- 人为规定max_heap元素个数>=min_heap 这样总个数为偶数时:返回(-l[0]+r[0])/2.0 奇数时直接返回-l[0]    
- 插入一个新数时 先插入max_heap(left) 然后再pop max_heap给min_heap 当r元素个数大于l时 再pop回l
这样可以做到 len(max_heap) >= len(min_heap) (最多多一个元素)
注意入堆时元素的正负 最大堆要负号入堆
T(logn) for add, T(1) for find. S(n) 
'''
class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0 
        else:
            return -self.max_heap[0]
