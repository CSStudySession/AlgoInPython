'''
variant: create an Iterator that utilizes next() and hasNext() functions 
to perform post-order traversal on the binary tree.
思路:使用stack来模拟递归过程 并用一个变量last_visited记录上一次访问的节点
每次peek当前栈顶元素node
如果node没有左右孩子 或者左右孩子都访问过了 则可以“访问”当前节点->即next()
否则 按“左→右→根”的顺序往栈里压入它的左右子树
核心变量: current当前还没有被压入栈的节点 是我们准备“往左走”探索的节点 为None的话就切到右子树
T(1) amertized, T(h) for worst case. S(h) 最多存从根到某一条叶子的路径
'''
class PostorderIterator:
    def __init__(self, root):
        self.stack = []
        self.last_visited = None
        self.current = root
    def hasNext(self):
        return self.current is not None or len(self.stack) > 0
    def next(self):
        while self.hasNext():
            # 不断往左走 把路径压栈
            if self.current:
                self.stack.append(self.current)
                self.current = self.current.left
            else:
                peek_node = self.stack[-1]
                # 右子树存在 且还没访问过 则往右走
                if peek_node.right and self.last_visited != peek_node.right:
                    self.current = peek_node.right
                else:
                    # 否则可以访问当前节点
                    self.last_visited = self.stack.pop()
                    return self.last_visited
        raise ValueError("No more elements")