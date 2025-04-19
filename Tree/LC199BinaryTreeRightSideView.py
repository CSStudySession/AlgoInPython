from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
思路: BFS
BFS遍历每层节点 每层最后一个节点即为right side view能看到的. 把它加到结果集中.
'''
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root: 
        return []
    queue = collections.deque([root])
    ret = []
    while queue:
        cur_len = len(queue)
        for i in range(cur_len): # 遍历当前层
            node = queue.popleft()
            if i == cur_len - 1: # 每层最后一个节点的值 即为从右往左能看到的值
                ret.append(node.val)
            # 有左右子节点 就入队
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ret