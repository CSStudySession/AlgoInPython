
from typing import Optional, List, collections

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    ret = []
    # {col_idx, [list of nodes with column idx as col_idx]}
    node_dict = collections.defaultdict(list) # dict不是Python keywords, 但不推荐作为变量名
    queue = collections.deque([(root, 0)]) # 括号里是[(x,y)]形式. root col_idx as 0
    min_col, max_col = 0, 0

    while queue:
        node, idx = queue.popleft() # front is at the right-end
        min_col = min(idx, min_col)
        max_col = max(idx, max_col)
        if node.left:
            queue.append((node.left, idx - 1))
        if node.right:
            queue.append((node.right, idx + 1))
            node_dict[idx].append(node.val)
    
    for i in range(min_col, max_col + 1):
        ret.append(node_dict[i])
    
    return ret