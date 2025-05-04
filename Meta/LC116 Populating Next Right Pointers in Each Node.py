from typing import Optional
import collections
'''

'''
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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