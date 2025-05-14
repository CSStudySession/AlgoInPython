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

'''
Given the root of a binary tree, imagine yourself standing on theright side of it,
and your best friend standing on the left side, both observing the tree from their respective sides.
Return the values of the nodes you can both see, first from the left side (bottom to top),
followed by those from the right side(top to bottom)
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [5,2,1,3,4]
    1
  2   3 
 n 5 n  4     
Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [5,4,2,1,3]
思路: BFS. 维护两个list 分别记录bfs每层的第一个元素(left view)和最后一个元素(right view)
bfs结束后 reverse left view list 然后append上right view list的除去第一个元素(x[1:])
T(n) S(n)
'''
def tree_left_right_side_view(root:Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    left_side, right_side = [], []
    queue = collections.deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                left_side.append(node.val)
            if i == size - 1:
                right_side.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    left_side.reverse()
    left_side.extend(right_side[1:])
    return left_side

'''
variant2: same setup as variant 1 but to print out the both views.
'''
def print_tree_both_side_view(root:Optional[TreeNode]) -> None:
    if not root:
        return []
    left_side, right_side = [], []
    queue = collections.deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                left_side.append(node.val)
            if i == size - 1:
                right_side.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    for j in range(len(left_side) - 1, -1, -1):
        print(left_side[j], " ")
    for k in range(1, len(right_side)):
        print(right_side[k], " ")

'''
variant3: solve it in DFS
思路:用一个right_view数组 跟着dfs 用一个参数level记录当前dfs层数 
每次层数==len(view)时 把node值加入view 然后递归先看右子树 再看左子树 保证先看右边
T(n) S(H),H worst is N
'''

def right_side_view_dfs(root:Optional[TreeNode]) -> list[int]:
    right_view = []
    dfs_right_view(root, right_view, 0)
    return right_view

def dfs_right_view(node:TreeNode, right_view:list[int], level:int) -> None:
    if not node:
        return
    if level == len(right_view):
        right_view.append(node.val)
    dfs_right_view(node.right, right_view, level + 1)
    dfs_right_view(node.left, right_view, level + 1)