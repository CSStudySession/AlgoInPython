from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# LC origin. T(Nlog(k)) S(k) k: number of lists
ListNode.__lt__ = lambda x, y: (x.val < y.val) # 必须要写 heap需要用比较器
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    import heapq
    heap = []
    dummy = ListNode(0)
    cur = dummy
    
    for head in lists:
        if head: # 注意检查 否则会把None放入heap
            heapq.heappush(heap, head) # 用到了__lt__
    while heap:
        node = heapq.heappop(heap)
        cur.next = node 
        if node.next: # 检查从heap弹出node的下一个是否存在
            heapq.heappush(heap, node.next)
        cur = cur.next # cur要走一步
    return dummy.next

# variant 1: input is a list of int arrays, or 2D list of intervals.
# note that it may ask to remove dulicates.
# 思路:创建辅助结构体 构建{列表id, 当前列表元素id, 元素值} 把该结构体对象入堆
# T(Nlog(k)) S(k) k: number of lists, N: number of elements
class Item:
    def __init__(self, list_id:int=0, idx:int=0, val:int=0):
        self.list_id = list_id
        self.idx = idx
        self.val = val
    def __lt__(self, other: 'Item'):
        return self.val < other.val

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, Item(i, 0, lists[i][0]))
    ret = []
    while heap:
        list_id, idx, val = heapq.heappop(heap)
        ret.append(val)
        idx += 1
        if idx < len(lists[list_id]):
            heapq.heappush(heap, Item(list_id, idx, lists[list_id][idx]))
    return ret

# variant 2: implement the Iterator class that represents an iterator over
# the array of integer arrays. 实现几个Iterator的接口. 用到variant 1的Item类
class KListIterator:
    def __init__(self, lists: List[List[int]]):
        self.heap = []
        self.lists = lists
        for i in range(len(lists)): # 每个子list的头元素入堆
            if lists[i]:
                heapq.heappush(self.heap, Item(i, 0, lists[i][0]))
    
    # return True if there exits at least one integer in an array, False otherwise
    def hasNext(self) -> bool:
        return False if not self.heap else True
    
    # moves pointer forward by one, then returns lowest valued int at pointer.
    # throw error if there's none.
    def next(self) -> int:
        if not self.hasNext():
            raise ValueError("no elements left")
        list_id, idx, val = heapq.heappop(self.heap)
        idx += 1 # 注意这里要移动指针
        if idx < len(self.lists[list_id]): # 当前list的下一个元素入堆
            heapq.heappush(self.heap, Item(list_id, idx, self.lists[list_id][idx]))
        return val
    
# variant 3: input is a list of int arrays, and a int k. return kth smallest number.
# 思路:min-heap 每个array的第一个元素入堆 然后heap pop and push 直到pop到k次 当前值即为答案.
# 注意这是k-way merge问题 与top-k问题有本质区别. 本问题无法剪枝:所有数组都要入堆
# T((k+n) log(n)) k是目标的位置 n是数组个数  S(n) 每个数组最多一个元素在堆中
def get_kth_item(lists: List[List[int]], k: int) -> int:
    if not lists:
        return -1
    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, Item(i, 0, lists[i][0]))
    
    cnt = 0
    while heap: # heap pop until cnt == k
        curr = heapq.heappop(heap)
        cnt += 1
        if cnt == k:
            return curr.val
        idx = curr.idx + 1
        if idx < len(lists[curr.list_id]):
            heapq.heappush(heap, Item(curr.list_id, idx, lists[curr.list_id][idx]))
    return -1