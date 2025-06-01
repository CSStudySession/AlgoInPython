'''
求两个点的最近公共祖先: 无parent pointer, 有root
在root为根的二叉树中找A,B的LCA:
如果找到了就返回这个LCA
如果只碰到A 就返回A 如果只碰到B 就返回B. 如果都没有 就返回null
'''
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if not root: return None
    if root == q or root == p: return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right: # LCA即为root 且在p,q的上面
        return root
    #如果只有一边有东西 只需要return有东西的一边
    if left: return left
    if right: return right
    return None

'''
variant1: given a N-ary tree. return LCA. 思路: dfs
1. dfs构建父节点映射表(dict) 直到找到p和q.
2. 用set收集p的所有祖先
3. 沿着q的路径向上找 直到找到一个在p祖先集合中的节点 即为LCA.
'''
class TreeNode:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

def lca_n_ary_tree(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent = {root: None} # 记录节点:parent
    stack = [root]
    while p not in parent or q not in parent: # 'or'确保同时找到p和q
        node = stack.pop()
        for child in node.children:
            parent[child] = node
            stack.append(child)
    ancestors = set() #记录p的所有祖先
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

'''
variant2: given a list of nodes. return LCA of them. 思路: post-order traversal
把 nodes 存入一个集合 target_set
从根节点 root 开始做后序遍历
 - 递归遍历左右子树。
 - 判断当前节点是否是 target_set 中的节点
 - 统计当前子树中出现了多少个 target 节点。
如果当前子树中包含所有的 k 个节点，且当前节点是第一个满足这个条件的节点，则它是 LCA。
T(n) S(n)
'''
def lowestCommonAncestor(root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
    target_set = set(nodes)
    ret = [None]
    dfs(root, target_set, ret)
    return ret[0]

def dfs(node, target_set, ret):
    if not node:
        return 0
    # 分别统计左右子树中 target 节点的数量
    left_count = dfs(node.left)
    right_count = dfs(node.right)
    # 当前节点是否是 target 节点
    cur = 1 if node in target_set else 0
    # 当前节点子树包含的 target 总数
    total = left_count + right_count + cur
    # 如果正好包含所有 target，且还未记录答案
    if total == len(target_set) and not ret[0]:
        ret[0] = node
    return total