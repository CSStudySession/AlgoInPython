from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# OG. T(k * N/klogN/k) + O(N) = O(NlogN/k), k:number of columns, O(N) for tree traversal
# S(n) n is # of nodes
def verticalTraversal_sort(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return [[]]
    col_to_val = collections.defaultdict(list) # dict的值:list of tuple
    queue = collections.deque([(root, 0,0)]) # (node, row_idx, col_idx)
    min_col, max_col = float('inf'), float('-inf') # float括号里是'inf'
    while queue:
        curr, i, j = queue.popleft()
        min_col = min(min_col, j)
        max_col = max(max_col, j)
        col_to_val[j].append((i, curr.val))
        if curr.left:
            queue.append((curr.left, i + 1, j - 1))
        if curr.right:
            queue.append((curr.right, i + 1, j + 1))
    ret = []
    for k in range(min_col, max_col + 1): # 遍历所有列.
        # tuple排序 默认先按第一个值 再按第二个值 (升序)
        ret.append([val for _, val in sorted(col_to_val[k])])
    return ret

# variant1: print the vertical order traversal, sperating each col by a newline.
# note: clarify the formatting before coding!
def vertical_print(root: Optional[TreeNode]) -> None:
    if not root:
        return
    col_to_val = collections.defaultdict(list) # dict的值:list of tuple
    queue = collections.deque([(root, 0,0)]) # (node, row_idx, col_idx)
    min_col, max_col = float('inf'), float('-inf') # float括号里是'inf'
    while queue:
        curr, i, j = queue.popleft()
        min_col = min(min_col, j)
        max_col = max(max_col, j)
        col_to_val[j].append((i, curr.val))
        if curr.left:
            queue.append((curr.left, i + 1, j - 1))
        if curr.right:
            queue.append((curr.right, i + 1, j + 1))
    for k in range(min_col, max_col + 1): # 遍历所有列.
        # tuple排序 默认先按第一个值 再按第二个值 (升序)
        print([val for _, val in sorted(col_to_val[k])])

# variant2: return vertical order traversal as a flat 1D list. 
# note: compare it with LC314.
def verticalTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    col_to_val = collections.defaultdict(list) # dict的值:list of tuple
    queue = collections.deque([(root, 0,0)]) # (node, row_idx, col_idx)
    min_col, max_col = float('inf'), float('-inf') # float括号里是'inf'
    while queue:
        curr, i, j = queue.popleft()
        min_col = min(min_col, j)
        max_col = max(max_col, j)
        col_to_val[j].append((i, curr.val))
        if curr.left:
            queue.append((curr.left, i + 1, j - 1))
        if curr.right:
            queue.append((curr.right, i + 1, j + 1))
    ret = []
    for k in range(min_col, max_col + 1): # 遍历所有列.
        # .extend()in-place更新一维列表 元素都往一个list里面塞
        # tuple排序 默认先按第一个值 再按第二个值 (升序)
        ret.extend([val for _, val in sorted(col_to_val[k])])
    return ret