'''
dfs 给左右孩子pass下去targetSum-node.val的值, 最后需要的是left or right 返回值or后返回
T(n) S(1)
'''
def hasPathSum(root, targetSum) -> bool:
    if not root: 
        return False
    if not root.left and not root.right: 
        return targetSum == root.val
    left = hasPathSum(root.left, targetSum - root.val)
    right = hasPathSum(root.right, targetSum - root.val)
    return left or right

