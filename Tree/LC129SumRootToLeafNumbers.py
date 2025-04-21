from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解法1 BFS. code适用于节点值是multi-digit的情况
def sumNumbers_bfs(root: Optional[TreeNode]) -> int:
    if not root: return 0
    total = 0
    queue = collections.deque([(root, root.val)]) # 队列元素是a list of tuple 

    while queue:
        node, pathSum = queue.popleft()
        if not node.left and not node.right:
            total += pathSum
            continue

        if node.left: # 注意这里append的是node.left/right val是node.left/right的
            queue.append((node.left, int(str(pathSum) + str(node.left.val))))
        if node.right:
            queue.append((node.right, int(str(pathSum) + str(node.right.val))))
    
    return total

# 解法2 DFS. code适用于节点值是multi-digit的情况
def sumNumbers_dfs(root: Optional[TreeNode]) -> int:
    if not root: return 0
    res = [] # 存储每一条从root到叶节点的值 最后对res内的值求和即为答案
    tmp = "" # the path from root to leaf
    dfs(root, res, tmp) 
    return sum(res)

def dfs(node: TreeNode, res: list, tmp: str) -> None:
    if not node.left and not node.right:
        tmp += str(node.val)
        res.append(int(tmp))
        return
    tmp += str(node.val)
    if node.left:
        dfs(node.left, res, tmp)  
    if node.right:
        dfs(node.right, res, tmp)



c1 = TreeNode(1)
c2 = TreeNode(11)
root = TreeNode(12, c1, c2)
print(sumNumbers_dfs(root))
print(sumNumbers_bfs(root))