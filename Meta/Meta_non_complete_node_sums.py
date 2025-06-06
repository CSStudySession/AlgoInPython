'''
Print the Sums of the Paths to Each Non-Complete Node in a Binary Tree
不确定"Non-Complete Node"定义是否包含leave nodes.分开两个实现.
思路: DFS 从根节点递归遍历整棵树 同时记录当前路径和 当遇到“非完全节点”时就打印路径和, 然后递归左右子树处理.
T(n)  S(h) worst N
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 包含叶子节点版本
def print_path_sums(root: TreeNode):
    def dfs(node, path_sum):
        if not node:
            return
        path_sum += node.val # 当前路径和更新
        # 判断是否是非完全节点
        is_non_complete = not (node.left and node.right)
        if is_non_complete:
            print(f"Path sum to non-complete node {node.val}: {path_sum}")
        # 递归左右子树
        dfs(node.left, path_sum)
        dfs(node.right, path_sum)
    dfs(root, 0) # 实际调用

# 不包含叶子节点版本
def print_path_sums_non_leave(root: TreeNode):
    def dfs(node, path_sum):
        if not node:
            return
        path_sum += node.val # 当前路径和更新
        # 判断是否是非完全节点
        has_left = node.left is not None
        has_right = node.right is not None
        is_non_complete = (has_left and not has_right) or (has_right and not has_left) 
        if is_non_complete:
            print(f"Path sum to non-complete node {node.val}: {path_sum}")
        # 递归左右子树
        dfs(node.left, path_sum)
        dfs(node.right, path_sum)
    dfs(root, 0) # 实际调用