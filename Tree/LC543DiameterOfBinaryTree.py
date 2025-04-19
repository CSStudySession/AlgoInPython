from typing import Optional
'''
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
'''
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
        self.maxHeight(root, ret) # 调用递归函数 结果存在ret[0]
        return ret[0] # 注意返回的是ret[0] 不是self.maxHeight()!

    def maxHeight(self, root, ret) -> int:
        if not root: return 0

        left_ret = self.maxHeight(root.left, ret)
        right_ret = self.maxHeight(root.right, ret)
        ret[0] = max(ret[0], left_ret + right_ret) # 注意这里没有+1.只是left+right 定义中length是按edge算 不是按nodes算

        return max(left_ret, right_ret) + 1 # 这里要+1.左右取较大的 加上自己返回