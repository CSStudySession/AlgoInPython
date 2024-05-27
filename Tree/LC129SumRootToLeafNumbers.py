from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        total = 0
        queue = collections.deque([(root, root.val)])

        while queue:
            node, pathSum = queue.popleft()
            if not node.left and not node.right:
                total += pathSum
                continue
            if node.left:
                queue.append((node.left, pathSum * 10 + node.left.val))
            if node.right:
                queue.append((node.right, pathSum * 10 + node.right.val))
        
        return total