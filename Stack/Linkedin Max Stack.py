'''
implement a max stack. Interfaces are given.


'''

from typing import TypeVar, Generic
from sortedcontainers import SortedSet
T = TypeVar('T')

# two stack approach
class MaxStack_A(Generic[T]):
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, to_push: T) -> None:
        self.stack.append(to_push)
        if not self.stack or to_push > self.max_stack[-1]:
            self.max_stack.append(to_push)

    def peek(self) -> T:
        return self.stack[-1] if self.stack else None

    def pop(self) -> T:
        if not self.stack:
            return None
        ret = self.stack.pop()
        if self.max_stack[-1] == ret:
            self.max_stack.pop()
        return ret

    def peekMax(self) -> T:
        return self.max_stack[-1] if self.max_stack else None

    def popMax(self) -> T:     # worse case O(n) time & O(n) space
        if not self.max_stack:
            return None
        tmp_stack = []
        while self.stack and self.max_stack[-1] != self.stack[-1]:
            tmp_stack.append(self.stack.pop())
        max_item = self.max_stack.pop()
        self.stack.pop()
        while tmp_stack:
            self.stack.append(tmp_stack.pop())
        return max_item            

class Node:
    def __init__(self, val: T =None):
        self.val = val
        self.prev, self.next = None, None
    
    # insert node to the left of self
    def append_left(self, node: 'Node'):
        last = self.prev
        if last:
            last.next = node
            node.prev = last
        node.next = self
        self.prev = node

    def remove(self):
        prev, next = self.prev, self.next
        prev.next = next
        next.prev = prev
        del prev
    
    def __hash__(self) -> T:  # 要overwrite __hash__() method 为了排序用 注意这里一定不能overwrite __eq__()
        return self.val

class MaxStack_B(Generic[T]):
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.sorted_set = SortedSet([], key=lambda x: x.val)

    def push(self, to_push: T) -> None:    # O(log(n)) time: sorted_set add()   
        node = Node(T)
        self.tail.append_left(node)
        self.sorted_set.add(node)            

    def peek(self) -> T:                  # O(1)
        return self.tail.prev.val

    def pop(self) -> T:                   # O(log(n)) comes from sorted_set.remove()                  
        last = self.tail.prev
        ret = last.val
        self.sorted_set.remove(last)
        last.remove()
        return ret

    def peekMax(self) -> T:             # O(1)
        return self.sorted_set[-1].val

    def popMax(self) -> T:              # O(log(n)) comes from sorted_set.remove()   
        node = self.sorted_set[-1]
        ret = node.val
        node.remove()
        self.sorted_set.remove(node)
        return ret
