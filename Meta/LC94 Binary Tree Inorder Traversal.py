from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right   
class Solution:
    # method 1: traverse: dfs左边->current->dfs右边 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
               
        self.traverse(root.left)
        self.res.append(root.val)
        self.traverse(root.right)
        
    # method 2: interative. stack
    # 先找到deep left node, until left tree is all done.  
    # find first right node, repeat finding deep left node.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res = []
        stack = []
        #1.确定起点: leftmost node
        while root:
            stack.append(root)
            root = root.left
        #2.pop element from stack and append to res. then check right node.
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                nextnode = node.right
                while nextnode:
                    stack.append(nextnode)
                    nextnode = nextnode.left
        return res
'''
variant:
Given a Binary Tree and an input array. 
The task is to create an Iterator that utilizes next() and hasNext() functions 
to perform Inorder traversal on the binary tree.
思路: 用栈来模拟中序遍历过程 left root right
每次next()调用:
- 从栈中弹出当前节点（即当前要访问的节点）
- 如果该节点有右子树 将右子树的左链路径压入栈中（即再走一段“左到底”的过程）
T(1) amertized, worst T(h) for a node with left path length h.
S(h) worst case would be n 
''' 
class InorderIterator:
    def __init__(self, root:TreeNode):
        self.traversal = [] # stack
        self.moveLeft(root)
 
    def moveLeft(self, current:TreeNode):
        while current != None:
            self.traversal.append(current)
            current = current.left
 
    def hasNext(self):
        return len(self.traversal) > 0
 
    def next(self):
        if not self.hasNext():
            raise Exception('No such element Exists')
        current = self.traversal.pop()
        if current.right != None:
            self.moveLeft(current.right)
        return current