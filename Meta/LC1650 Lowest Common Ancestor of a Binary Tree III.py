'''
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# method 1. 计算两个节点的深度. 深的节点往上跳 直到两个节点深度一致. 然后两个节点同时往上跳 汇合时即为LCA
# T: O(n)  S: O(1)
def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    p_depth = self.getDepth(p)
    q_depth = self.getDepth(q)

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

def getDepth(self, node):
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