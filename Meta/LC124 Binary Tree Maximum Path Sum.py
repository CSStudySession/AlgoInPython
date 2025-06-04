'''
使用Post-order DFS
对于每个节点，递归计算其左右子树向下延伸的最大贡献值。
如果某个子树返回负数 意味着它对路径是“减分项” 直接视作0 即 max(0, dfs(...))）
核心定义：
对于每个节点node 计算路径经过该节点的最大路径和为 left_sum + right_sum + node.val
用它试图更新全局最大值ret[0]
返回值设计：
每次递归返回从当前节点出发 向下延伸形成的最大路径和（只能走一条分支）
return max(left_sum, right_sum) + root.val
T(n) S(h) worst N
'''
def maxPathSum(root: Optional[TreeNode]) -> int:
    ret = [float('-inf')]
    dfs(root, ret)
    return ret[0]

def dfs(self, root, ret) -> int:
    if not root: return 0
    
    left_sum = max(0, self.dfs(root.left, ret))
    right_sum = max(0, self.dfs(root.right, ret))
    
    ret[0] = max(ret[0], left_sum + right_sum + root.val)
    
    return max(left_sum, right_sum) + root.val # path through current node to any leaf 