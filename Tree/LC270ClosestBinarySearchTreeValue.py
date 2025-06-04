from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 指针从root开始遍历, 逐个比较 不断更新res 注意diff相等的时候需要取小的值
# T(h), where h is height of tree and worst case is N. S(1)
def closestValue(root: Optional[TreeNode], target: float) -> float:
    ret = root.val
    while root:
        if root.val == target: return root.val
        if abs(root.val  - target) < abs(ret - target):
            ret = root.val
        elif abs(root.val  - target) == abs(ret - target):
            ret = min(root.val, ret) # diff一样取原始值小的

        if target < root.val:
            root = root.left
        else:
            root = root.right
    return ret

# variant: given target is an int value.
def closest_int_val(root: Optional[TreeNode], target: int) -> int:
    ret = root.val
    min_dist = float('inf')
    
    while root:
        if root.val == target: return root.val
        dist = abs(root.val - target)
        if dist < min_dist:
            ret = root.val
            min_dist = dist
        elif dist == min_dist: # diff一样取原始值小的
            ret = min(root.val, ret)

        if target < root.val:
            root = root.left
        else:
            root = root.right
    return ret