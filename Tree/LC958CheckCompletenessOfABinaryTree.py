from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
使用一个队列进行 BFS 层序遍历 允许None节点入队 表示空子节点
一旦遇到第一个None节点 标记seen_null=True
如果之后还遇到非空节点 说明有节点出现在了空节点之后 不符合完全二叉树的定义 直接返回False
如果整棵树遍历完都没有违反条件 说明是合法的 返回True
T(n) S(n) n为节点个数
'''
def isCompleteTree(root) -> bool:
    queue = deque([root])
    seen_null = False

    while queue:
        node = queue.popleft()
        if node is None:
            seen_null = True
        else:
            if seen_null:
                return False # 在见过null之后还出现了非null节点 不合法
            queue.append(node.left)
            queue.append(node.right)
    return True