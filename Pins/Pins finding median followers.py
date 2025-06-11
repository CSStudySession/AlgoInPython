'''
每个用户有一个follower数量 需要实现一个数据结构 支持两种操作:
add(elem)：插入一个用户的 follower 数
getMedian()：常数时间内返回当前集合中所有 follower 数的中位数。
输入:一系列 add(num)操作 num是一个整数
若干getMedian()查询
输出:对每次getMedian() 返回当前集合中所有元素的中位数
Clarifications
是否允许重复值？ 是的，允许。
输入是否一次性给出？否，支持流式添加。
是否支持删除？本题暂不支持删除 但follow-up会问
思路:two heaps.
'''
import heapq
class MedianFollowerTracker:
    def __init__(self):
        self.left_heap = []   # 最大堆 存较小一半（用负数）
        self.right_heap = []  # 最小堆 存较大一半
    # T(logN)
    def add(self, num):
        # 第一步 先插入最大堆
        heapq.heappush(self.left_heap, -num)

        # 第二步 把最大堆堆顶转移到最小堆
        max_left = -heapq.heappop(self.left_heap)
        heapq.heappush(self.right_heap, max_left)

        # 第三步：如果右边堆元素更多（超过1）把最小堆堆顶移回最大堆
        if len(self.right_heap) > len(self.left_heap):
            min_right = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -min_right)
    # T(1)
    def get_median(self):
        if not self.left_heap and not self.right_heap:
            raise Exception("No data")

        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2

'''
followup:
- 如果一次性给出所有值（不是流式添加）怎么办？
可以将所有值排序后直接线性读取中位数
时间复杂度 O(N logN)。
- 如何实现删除中位数？
不能直接删堆顶：删除后两个堆大小会不平衡
需要rebalance维护两个堆大小差不超过1
要考虑heap不支持任意元素删除(需要额外设计 如懒惰删除或索引映射)
'''