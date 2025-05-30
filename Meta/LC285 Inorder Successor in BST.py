'''
思路:因为 BST 有序（左 < 根 < 右）：
- 如果当前节点值 > p.val 它可能是后继 向左走
- 如果当前节点值 ≤ p.val 不可能是后继 向右走
沿途记录潜在的successor
T(h), h worst n, S(1)
'''
def inorderSuccessor(root, p):
    successor = None
    while root:
        if p.val < root.val:
            # 当前节点可能是后继，继续往左找
            successor = root
            root = root.left
        else:
            # 当前节点 ≤ p，说明后继一定在右子树
            root = root.right
    return successor

'''
variant: what if it's not a BST, just a general binary tree?
思路:in order dfs, keep track of a previous node along the way.
使用变量prev 记录上一个访问的节点
当发现prev==p时 当前节点就是答案
T(n) S(h) dfs stack length
'''
def inorderSuccessor(root, p):
    # 记录前一个访问节点
    prev = [None]
    ret = [None]
    inorder(p, root, prev, ret)
    return ret[0]

def inorder(p, node, prev, ret):
    if not node or ret[0]:
        return
    inorder(p, node.left, prev, ret)
    if prev[0] == p:  # 如果上一个节点是p 则当前节点是答案
        ret[0] = node
        return
    prev[0] = node
    inorder(p, node.right, prev, ret)