from typing import Optional
'''
思路:dfs+Memoization 枚举每个数i(从start到end)作为根节点
  - 将i左边的数构成左子树 递归生成[start, i-1]的所有BST
  - 将i右边的数构成右子树 递归生成[i+1, end]的所有BST
  - 遍历所有左子树与右子树组合 连接到当前根i上 组成一棵完整BST
  - 使用memo[(start, end)]缓存子问题结果 避免重复计算

T(Cₙ*n) 其中Cₙ是第n个Catalan number 表示不同BST的数量
对于每棵树需要最多O(n)的时间构造节点
Cₙ = (2n)! / (n!(n+1)!) 复杂度为O(4ⁿ/n^{1.5})
S(Cₙ*n) 用于存储所有可能的树结构 + 递归调用栈空间 + memo 字典
'''
def generateTrees(n: int) -> list[Optional[TreeNode]]:
    memo = {}
    return allPossibleBST(1, n, memo)

def allPossibleBST(start, end, memo):
    res = []
    if start > end:
        res.append(None)
        return res
    if (start, end) in memo:
        return memo[(start, end)]
    # Iterate through all values from start to end to construct left and right subtree recursively.
    for i in range(start, end + 1):
        leftSubTrees = allPossibleBST(start, i - 1, memo)
        rightSubTrees = allPossibleBST(i + 1, end, memo)
        # Loop through all left and right subtrees and connect them to ith root.
        for left in leftSubTrees:
            for right in rightSubTrees:
                root = TreeNode(i, left, right)
                res.append(root)
    memo[(start, end)] = res
    return res