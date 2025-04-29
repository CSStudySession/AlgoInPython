from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
# 三种情况: 
# 1. given head is None
# 2. insertVal >= max or inserVal <= min: 插入max->insertVal->min
# 3. 都不是 遍历找到插入点
def insert(head: 'Optional[Node]', insertVal: int) -> 'Node':
    to_insert = Node(insertVal)
    if not head:
        to_insert.next = to_insert # 要变成循环linkedlist
        return to_insert # 返回新节点
    
    cur = head
    while cur.next != head and cur.next.val >= cur.val: # cur停在max node
        cur = cur.next
    min_node = cur.next # 因为是循环linkedlist max的下一个是min
    
    if to_insert.val <= min_node.val or to_insert.val >= cur.val:
        cur.next = to_insert
        to_insert.next = min_node
        return head
    
    while cur.next.val <= to_insert.val: # 从最大节点开始找改插入的位置
        cur = cur.next
    to_insert.next = cur.next
    cur.next = to_insert
    return head