from typing import Optional
import collections
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
方法1:BFS
层序遍历tree 每层遍历时 从队列popleft出的节点 两种情况:
1.不是当前层最后一个节点.它的next此时还在队列中 就是队头元素queue[0]
2.是最后一个节点.它next是null 不用处理
bfs过程中 用下表判断当前节点是否是当前层最后一个
T(n) S(n)
'''
def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    queue = collections.deque([root])
    while queue:
        size = len(queue)
        for idx in range(size):
            cur = queue.popleft()
            if idx != size - 1:
                cur.next = queue[0]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
    return root

'''
方法2: using last connected next pointers
based on observation, 2 types of next connection for node a/b at same level:
1. node a/b have same parent: parent.left.next = parent.right
2. node a/b have diff parent. say b is to the right of a. 
     x        y      x.right是a  y.left是b  x.next是y
       a    b
此时: x.right.nxt=x.next.left; x=x.next
T(n) S(1)
'''
def connect_v1(root:'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    left_most = root # 用一个ref一直从左边往左下移动 模拟层序遍历
    while left_most.left:
        cur = left_most
        while cur:
            cur.left.next = cur.right # connection 1
            if cur.next:
                cur.right.next = cur.next.left # connection 2
            cur = cur.next # cur往右走一步 处理右子树
        left_most = left_most.left
    return root