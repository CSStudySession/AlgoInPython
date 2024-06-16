from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    # 三种情况: 
    # 1. no head
    # 2. insertVal >= max or inserVal <= min: 插入max->insertVal->min
    # 3. 都不是 就直接插入
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        cur_node = Node(insertVal)
        if not head:
            cur_node.next = cur_node
            return  cur_node
        
        dummy = Node(-1)
        dummy.next = head

        # find min and max value nodes
        while head.next != dummy.next and head.val <= head.next.val:
            head = head.next
        min = head.next     # head stops at max

        if head.val <= insertVal or insertVal <= min.val:
            cur_node.next = min
            head.next = cur_node
        else:
            while head.next.val < insertVal:
                head = head.next
            cur_node.next = head.next
            head.next = cur_node
        return dummy.next

        
