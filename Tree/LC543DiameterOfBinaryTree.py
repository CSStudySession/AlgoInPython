from typing import Optional
'''
The diameter of a binary tree is the length of the longest path 
between any two nodes in a tree. 
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
variant1: given a N-ary tree and return the diameter.
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

'''
variant2: find the diameter, but all the nodes on the diameter path need to have 
the same value. e.g.:
          3a
    3b         3d
 1    3c     4    5
diameter is:3, formed by: 3c->3d->3a->3d 值全都得一样才行 
思路:同原题思路 变化是 在dfs处理当前node时 加个判断:自己的左右孩子与自己的val一样 才能延伸路径
不一样的话 return 0
T(n) S(h) worst n
'''
def longestUnivaluePath(root: TreeNode) -> int:
    ret = [0]
    def dfs(node, ret):
        if not node:
            return 0
        # 后序遍历
        left = dfs(node.left, ret)
        right = dfs(node.right, ret)
        # 如果子节点存在且值相同，则延伸路径
        left_path = right_path = 0
        if node.left and node.left.val == node.val:
            left_path = left + 1
        if node.right and node.right.val == node.val:
            right_path = right + 1
        # 更新全局最大路径
        ret[0] = max(ret[0], left_path + right_path)
        # 返回给父节点的最长单边路径
        return max(left_path, right_path) # 更新l/r_path时 只有与左/右值一样才能+1 否则就是0
    dfs(root, ret)
    return ret[0]

'''
variant3: same setup as OG but return longest diameter path
思路: 使用DFS后序遍历 在每个节点处计算:
- 当前节点左子树的最大高度 left_height
- 当前节点右子树的最大高度 right_height
- 以当前节点为中心的路径长度为 left_height + right_height
- 维护全局最大直径
  - 用一个引用变量 diameter[0] 记录全局最大直径值 当某个节点的left + right 超过当前最大值时 更新它
- DFS返回每个节点向下的最长路径(用于拼接) 同时通过best_path[0]存储历史上的最长路径
T(n) S(h), worst n
'''
def diameterOfBinaryTreeWithPath(root: Optional[TreeNode]) -> list[int]:
    diameter = [0]
    best_path = [[]]  # 用 list 包住 path 作为引用传递
    dfs(root, diameter, best_path)
    return best_path[0]

def dfs(node: Optional[TreeNode], diameter, best_path_holder) -> tuple[int, list[int]]:
    if not node:
        return 0, []
    # 左子树
    left_height, left_path = dfs(node.left, diameter, best_path_holder)
    # 右子树
    right_height, right_path = dfs(node.right, diameter, best_path_holder)

    # 如果当前节点能更新最大直径，更新 diameter 和 best_path_holder
    if left_height + right_height > diameter[0]:
        diameter[0] = left_height + right_height
        best_path_holder[0] = left_path + [node.val] + right_path

    # 返回当前节点向下的最长路径（给父节点接）
    if left_height > right_height:
        return left_height + 1, left_path + [node.val]
    else:
        return right_height + 1, right_path + [node.val]