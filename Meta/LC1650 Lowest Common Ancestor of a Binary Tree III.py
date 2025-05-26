'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
note: if val type is char, the solution still holds.
有parent 没有root.
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# method 1. 计算两个节点的深度. 深的节点往上跳 直到两个节点深度一致. 然后两个节点同时往上跳 汇合时即为LCA
# T: O(n)  S: O(1)
def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    p_depth = getDepth(p)
    q_depth = getDepth(q)

    # 更深的节点向上移动 直到same level
    for _ in range(p_depth - q_depth):
        p = p.parent
    for _ in range(q_depth - p_depth):
        q = q.parent
    
    # at the same level, return until they meet. 
    while p != q:
        p = p.parent
        q = q.parent
    return p

    # followup: what if p/q can be at different trees? 如果在同一棵树上
    # 最终的lca一定是非空且p==q, 在不同树上 一定至少有一个先走到None 或者两个一起走到None
#    while p and q and p != q:
#        p = p.parent
#        q = q.parent
#    return None if not p or not q else p

def getDepth(node):
    dep = 0
    while node:
        dep += 1
        node = node.parent
    return dep

# method 2: 用set存储p的所有parents. q向上找, 如果parent in set, 则是LCA
# T: O(n)  S: O(n)
def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    if not p or not q: return None
    parentSet = set()
    while p:
        parentSet.add(p)
        p = p.parent

    while q:
        if q in parentSet:
            return q
        else:
            q = q.parent
    return None

'''
varint:What if you were given all the nodes as a part of a vector, and no longer the root node?
给list of nodes, nodes是乱序的.Node对象只有左右孩子指针 没有parent指针, 整体没有root.
思路:
1. 遍历list 构造node-to-parent关系 用dict存这个关系.
2. 利用交替指针法 两个新指针起点分别是p,q 然后沿着dict往上trace parent, 直到两指针相遇即为lca.
 - 当某个指针比如p,走到头(即root节点 不在dict中) 把p指向q “交替指针” 最终一定相遇
T(n) S(n)
'''
def find_lca_given_list_node(nodes:list[Node], p:Node, q:Node) -> Node:
    node_to_parent = {}
    for node in nodes:
        if node.left:
            node_to_parent[node.left] = node
        if node.right:
            node_to_parent[node.right] = node
    
    cur_p, cur_q = p, q # 两个新ref 起点p,q
    while cur_p != cur_q: # 相遇时即为lca
        if cur_p in node_to_parent:
            cur_p = node_to_parent[cur_p]
        else: # 走到root节点 没有parent 重置为对面的起点
            cur_p = q
        
        if cur_q in node_to_parent:
            cur_q = node_to_parent[cur_q]
        else:
            cur_q = p
    return cur_p