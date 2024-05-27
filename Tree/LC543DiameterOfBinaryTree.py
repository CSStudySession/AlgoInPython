from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ret = [0]
        self.maxHeight(root, ret)
        return ret[0]

    def maxHeight(self, root, ret) -> int:
        if not root: return 0

        left_ret = self.maxHeight(root.left, ret)
        right_ret = self.maxHeight(root.right, ret)
        ret[0] = max(ret[0], left_ret + right_ret)

        return max(left_ret, right_ret) + 1