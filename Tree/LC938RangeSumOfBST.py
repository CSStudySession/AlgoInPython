from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# meta variant 1: return the average of all nodes with a value in range [low, high]
# calarify: the avg is float?
def rangeSumBST_bfs(root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ret = 0.0
        cnt = 0.0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ret += node.val
                cnt += 1
            if node.right and node.val < high: # node值在范围内 node.right/left才可能在范围内
                stack.append(node.right)
            if node.left and node.val > low:
                stack.append(node.left)
        return ret / cnt

# meta variant 2: we could call the function 10^4 times with different [low, high] given.
# 思路:前缀和 + 二分
# 对bst进行in-order traversal 转化成一个有序数组arr O(n) (多次query 但这步只用跑一次)
# 对arr求前缀和 得到前缀和数组prefix O(n) (多次query 但这步只用跑一次)
# 对一个query[low,high]: 在arr上进行二分 找到大于等于low的第一个下标a 和 小于等于high的第一个下标b
# ret = prefix[b] - prefix[a-1]
class MultiQueryBSTSum:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.prefix = []
        self.in_order_traversal(root)
        self.get_prefix()

    def in_order_traversal(self, root): # 中序遍历 node的值都存入arr
        if not root:
            return
        self.in_order_traversal(root.left)
        self.arr.append(root.val) # 这里可以顺带把prefix_sum更新了
        self.in_order_traversal(root.right)
    
    def get_prefix(self): # 求前缀和数组prefix
        self.prefix = [0] * (len(self.arr) + 1) # 多一个位置给前0项和
        for i in range(1, len(self.prefix)):
            self.prefix[i] = self.prefix[i - 1] + self.arr[i - 1]

    def get_range_sum(self, lo:int, hi:int) -> int:
        if lo < hi or lo > self.arr[-1] or hi < self.arr[0]: # [lo,hi]与BST没交集
            return 0
        # 找大于等于low的第一个下标
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right) // 2
            if self.arr[mid] < lo:
                left = mid + 1
            else:
                right = mid
        left_idx = right # 记下大于等于low的第一个下标

        #找小于等于high的第一个下标
        left, right = 0, len(self.arr) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.arr[mid] <= hi:
                left = mid
            else:
                right = mid - 1  
        right_idx = right # 记下小于等于high的第一个下标

        return self.prefix[right_idx + 1] - self.prefix[left_idx]

# 解法1: dfs. 递归函数定义:返回以当前节点为根的子树的 range sum BST.
def rangeSumBST_dfs(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root: return 0
    if root.val < low:      # 当前root小了 在范围外 应该往右走
        return rangeSumBST_dfs(root.right, low, high)
    if root.val > high:     # 当前root大了 在范围外 应该往左走
        return rangeSumBST_dfs(root.left, low, high) 
    # 当前root值在给定范围内 可以放到和里 然后递归求左边和右边 
    return root.val + rangeSumBST_dfs(root.left, low, high) + rangeSumBST_dfs(root.right, low, high)
# 解法2: bfs 用stack T(N) S(N) 
def rangeSumBST_bfs(root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ret = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ret += node.val
            if node.right and node.val < high: # node值在范围内 node.right/left才可能在范围内
                stack.append(node.right)
            if node.left and node.val > low:
                stack.append(node.left)
        return ret
