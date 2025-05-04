class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
1. 在 BST 中，对于任意一个节点 node:
- 如果 p.val 和 q.val 都小于 node.val 那么它们的 LCA 一定在 node 的左子树
- 如果 p.val 和 q.val 都大于 node.val 那么它们的 LCA 一定在 node 的右子树
如果 p.val <= node.val <= q.val 或 q.val <= node.val <= p.val 那么 node 就是它们的最近公共祖先
2. 从根节点开始 根据上述逻辑不断向左右子树遍历 直到找到第一个“分叉点”
T(N) S(1) 最差情况 树是一条线
'''
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # 获取 p 和 q 的值
    p_val = p.val
    q_val = q.val
    # 从根节点开始遍历
    node = root
    while node:
        # 当前节点的值
        parent_val = node.val
        if p_val > parent_val and q_val > parent_val:
            # 如果 p 和 q 都在当前节点的右子树
            node = node.right
        elif p_val < parent_val and q_val < parent_val:
            # 如果 p 和 q 都在当前节点的左子树
            node = node.left
        else:
            # 当前节点就是分叉点，即最近公共祖先
            return node