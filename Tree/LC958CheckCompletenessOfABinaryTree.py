from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        seen_null = False
        queue = collections.deque([root])
        while queue:
            if seen_null:
                return not any(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    seen_null = True
                else:
                    if seen_null:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
        return True