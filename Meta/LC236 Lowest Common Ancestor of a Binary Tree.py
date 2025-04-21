'''
求两个点的最近公共祖先: 无parent pointer, 有root
在root为根的二叉树中找A,B的LCA:
如果找到了就返回这个LCA
如果只碰到A 就返回A 如果只碰到B 就返回B. 如果都没有 就返回null
'''
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if not root: return None
    if root == q or root == p: return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right: # LCA即为root 且在p,q的上面
        return root
    #如果只有一边有东西 只需要return有东西的一边
    if left: return left
    if right: return right
    return None