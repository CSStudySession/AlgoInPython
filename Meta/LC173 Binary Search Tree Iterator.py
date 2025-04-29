from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 维护一个stack stack top的node 是当前BST子树中值最小的
# 初始化时 先把所有左边的节点亚栈
# next()时 当前节点出栈 如果有右孩子(一定没有左孩子 有的话会在它之前出栈)
# 把右孩子和右孩子所有的左孩子 入栈
# next() amertized T(1) (worse T(N)), hasNext() T(1)
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        val = self.stack[-1].val
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return val

    def hasNext(self) -> bool:
        return True if self.stack else False