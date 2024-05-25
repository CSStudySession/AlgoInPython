from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 指针从root开始遍历, 逐个比较 不断更新res, 注意diff相等的时候需要取小的值
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root.val == target: return target

        ret = root.val
        while root:
            if abs(root.val  - target) < abs(ret - target):
                ret = root.val
            elif abs(root.val  - target) == abs(ret - target):
                ret = min(root.val, ret)

            if target < root.val:
                root = root.left
            else:
                root = root.right
        return ret