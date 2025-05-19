'''
1. 如果当前节点有右子树 那么中序遍历中下一个访问的节点 一定是其右子树中最左边的节点
2. 如果没有右子树 就要从当前节点往上回溯 寻找第一个把当前节点作为“左子节点”的祖先
往上找第一个“左拐”的祖先节点 e.g.下面的例子: 15 -> 10 -> 20 20即为答案
       20
      /  \
    10    30
      \
      15 
T(h) worst n, S(1)
'''
def inorderSuccessor(node: 'Node') -> 'Node': # 不需要比较值 BST有位置信息
    if node.right: # 有右子树
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node == node.parent.right: # 往上找 第一个左拐的祖先
        node = node.parent
    return node.parent