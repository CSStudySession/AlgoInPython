from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
       
        if not root: return 0

        if root.val < low:      # 当前root小了 在范围外 应该往右走
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:     # 当前root大了 在范围外 应该往左走
            return self.rangeSumBST(root.left, low, high) 
        # 当前root值在给定范围内 可以放到和里 然后递归求左边和右边 
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)