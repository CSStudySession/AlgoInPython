from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
中序遍历整棵树（左 → 根 → 右），访问顺序就是我们链表的顺序
使用两个指针：
- prev 指向中序遍历中的前一个节点
- head 指向双向链表的头节点（即最左边的节点）
在每次遍历到一个节点时 将其与prev双向连接
最后 将head和最后一个节点prev互相连接 形成循环结构
解法适用于general binary tree in order, not only for BST
T(n) S(n)
'''
class Solution:
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