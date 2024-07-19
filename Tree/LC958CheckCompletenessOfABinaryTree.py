from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
bfs层序遍历:check valid nodes layer by layer
大体思想: 每层从左到右检查 是否是"complete" 检查过程中每个节点左右孩子入队构建下一层bfs 几个小细节见代码里的注释
'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        seen_null = False
        queue = collections.deque([root])
        while queue:
            if seen_null: # 当前是个null结点 如果当前层还有其他非null的结点 说明一定不满足条件 直接返回false
                return not any(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:    # 如果当前是null 记录一下见过null 但是不能直接返回 因为可能是最后一层 后面接着判断
                    seen_null = True
                else:
                    if seen_null: # 当前点不是null 之前见过null->"不complete"
                        return False
                    queue.append(node.left)   # 左右children入队
                    queue.append(node.right)
        return True  # 查了所有layer都没问题 返回