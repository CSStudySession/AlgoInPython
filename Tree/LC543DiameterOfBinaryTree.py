from typing import Optional
'''
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, children=None):
        self.val = val
        self.left = left
        self.right = right
        self.chilren = children if children else []

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    if not root: return 0
    ret = [0]
    maxHeight(root, ret) # 调用递归函数 结果存在ret[0]
    return ret[0] # 注意返回的是ret[0] 不是maxHeight()!

def maxHeight(root, ret) -> int:
    if not root: return 0

    left_ret = maxHeight(root.left, ret)
    right_ret = maxHeight(root.right, ret)
    ret[0] = max(ret[0], left_ret + right_ret) # 注意这里没有+1.只是left+right 定义中length是按edge算 不是按nodes算

    return max(left_ret, right_ret) + 1 # 这里要+1.左右取较大的 加上自己返回
    
'''
variant: given a N-ary tree and return the diameter.
思路: dfs with backtrack. 对node_x 设有3个chilren:
        node_x
     c1   c2   c3
循环遍历c1-->c3 求得每个c的最长path 记录top 2 length of path: max, second
则当前见过的最长diameter=max+second,node_x返回给上层max+1(包含自己这条边)
注意如何在递归中存diameter:用一个list ret, 可以动态更新ret[0]
T(n) S(n)
'''
def diameter_n_ary_tree(root: Optional[TreeNode]) -> int:
    if not TreeNode:
        return 0
    ret = []
    get_diameter(root, ret)
    return ret[0]

def get_diameter(node: Optional[TreeNode], ret:list[int]) -> int:
    if not node:
        return 0
    max_len, second_len = 0, 0
    for child in node.chilren:
        cur_len = get_diameter(child, ret)
        if cur_len > max_len:
            second_len, max_len = max_len, cur_len
        elif cur_len > second_len:
            second_len = cur_len
    ret[0] = max(ret[0], max_len + second_len)
    return max_len + 1