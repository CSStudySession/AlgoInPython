from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  
class Solution:
    # method 1: traverse
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res
    
    def traverse(self, root): # 自己->dfs左子树->dfs右子树
        if not root:
            return
        self.res.append(root.val)    
        self.traverse(root.left)
        self.traverse(root.right)

# method2: interative(stack)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return [] # must have 否则root.val invalid
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
'''
variant:
Given a Binary Tree and an input array. 
The task is to create an Iterator that utilizes next() and hasNext() functions 
to perform pre-order traversal on the binary tree.

思路：
访问顺序：根 -> 左 -> 右
使用一个栈 stack 保存待访问的节点。
初始化时将 root 入栈
next() 时弹出栈顶节点作为当前节点 并按顺序将其右孩子先入栈 再将左孩子入栈 保证左子树先被访问
hasNext() 判断栈是否为空
'''
class PreorderIterator:
    def __init__(self, root: TreeNode):
        # 用列表模拟栈，存放待访问的节点
        self.stack = []
        if root:
            self.stack.append(root)  # 初始化时将根节点入栈

    def hasNext(self) -> bool: #T(1)
        # 栈非空说明还有下一个节点
        return len(self.stack) > 0

    def next(self) -> TreeNode: # T(1)
        if not self.hasNext():
            raise Exception('No such element Exists')
        # 弹出栈顶节点作为当前访问节点
        current = self.stack.pop()
        # 先压入右子节点，再压入左子节点
        # 这样下次 pop 时会先访问左子树
        if current.right:
            self.stack.append(current.right)
        if current.left:
            self.stack.append(current.left)
        return current