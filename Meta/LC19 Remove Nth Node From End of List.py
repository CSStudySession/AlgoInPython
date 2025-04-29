class Node:
    def __init__(self, val:int=0, next:'Node'=None):
        self.val = val
        self.next = next
'''
- 首先创建一个虚拟头节点dummy并将它指向原链表的头节点head 为了处理可能需要删除头节点的情况。
- 设置两个指针first和second 初始时都指向虚拟头节点dummy。
- 将first指针向前移动n+1步 而不是n步 这里的"+1"是因为我们需要找到要删除节点的前一个节点 以便修改指针
- 然后同时移动first和second指针 保持它们之间的距离始终为n+1个节点 直到first指针到达链表末尾 即first为None
- 此时 second指针正好指向倒数第n+1个节点 也就是要删除节点的前一个节点。
- 执行删除操作 second.next = second.next.next 跳过倒数第n个节点。
最后返回dummy.next 即为修改后的链表头节点。
T(N) N is num of nodes. S(1)
'''
def remove_nth_from_end(head, n):
    dummy = Node(-1)
    dummy.next = head
    slow, fast = dummy, dummy
    for _ in range(n + 1): # 走n+1步
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next