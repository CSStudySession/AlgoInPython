from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method 1: DFS in-order traverse a tree, get a node list. 
    # then link each node, and link head and tail. ->need extra space O(n)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        head, prev = [None], [None]
        self.dfs(root, head, prev)
        prev[0].right = head[0]
        head[0].left = prev[0]
        return head[0]
    
    def dfs(self, node: Node, head: List[Node], prev: List[Node]):
        if not node: return
        
        self.dfs(node.left, head, prev)

        if prev[0]:   # 存在之前的结点(值比当前结点小的结点) 连接node和prev[0]
            prev[0].right = node
            node.left = prev[0]
        else:         # 之前结点不存在: 当前结点为值最小的点 记为head
            head[0] = node
        prev[0] = node   # prev[0]往前移动一个 作为下一个节点的左边节点

        self.dfs(node.right, head, prev)