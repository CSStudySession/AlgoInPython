from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # method 1: DFS in-order traverse a tree, get a node list. 
    # then link each node, and link head and tail. ->need extra space O(n)
    # method 2: stack
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
       
        head, prev = [None], [None]
        self.dfs(root, head, prev)
    
        prev[0].right = head[0]
        head[0].left = prev[0]
        return head[0]
    
    def dfs(self, node, head, prev):
        if not node: return
        
        self.dfs(node.left, head, prev)
        
        if prev[0]:
            prev[0].right = node
            node.left = prev[0]
        else:
            # this is the head
            head[0] = node
        
        # 更新prev为当前的node --> 下一次node的left
        prev[0] = node

        self.dfs(node.right, head, prev)