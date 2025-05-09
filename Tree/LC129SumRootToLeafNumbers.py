from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# OG 思路:BFS. multi-digit的情况 不要用字符串拼接的方式做 面试时会被reject. 
# T(n) S(n)
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
            queue.append((node.left, pathSum * 10 + node.left.val))
        if node.right:
            queue.append((node.right, pathSum * 10 + node.right.val))
    return total

'''
variant1: value of nodes can contain any number from [0,999]
思路:dfs
1.每访问一个节点 用get_factors方法得到其位数(返回10的若干次方)
2.拼接当前路径数字 cur = cur * factors + node.val
3.如果当前是叶子节点 则加到总和中
T(n) S(n)
'''
def sum_dfs(root: Optional[TreeNode]) -> int:
    return dfs(root, 0)

def dfs(node: TreeNode, cur: int) -> int:
    if not node:
        return 0
    factors = get_factors(node.val)
    cur_sum = cur * factors + node.val
    if not node.left and not node.right: # 叶节点返回整条路径值
        return cur_sum
    # 否则递归左右子树
    left_sum = dfs(node.left, cur_sum)
    right_sum = dfs(node.right, cur_sum)
    return left_sum + right_sum # 递归回来返回左右子树之和

def get_factors(value: int) -> int:
    if value == 0:
        return 10
    factors = 1
    while value:
        value //= 10
        factors *= 10
    return factors

c1 = TreeNode(1)
c2 = TreeNode(11)
root = TreeNode(12, c1, c2)
print(sum_dfs(root))
print(sumNumbers_bfs(root))

'''
variant2: given the root of a binary tree containing digits from -9 to 9 only.
Each root-to-leaf path in the tree represents a number whose sign is negative 
if there is an odd number of negative nodes in the path, and conversely positive 
if there is an even number of negative nodes in the path.
These are known as a negative path and a positive path, respectively.
For example, the root-to-leaf path 1 ->-2 -> 3 represents thenumber -123. return sum of root to leaf.
思路:DFS遍历所有从根到叶子的路径
- 记录当前路径对应的数字（将节点的绝对值按位拼接）
- 同时记录路径中负数的数量（用来确定符号）
- 到达叶子节点时 根据负数数量决定正负号 加入总和
- 不是叶节点 递归计算左右子树
T(n) S(n)
'''
def sum_nums(root:TreeNode) -> int:
    return dfs(root, 0, 0)

def dfs(node:TreeNode, cur_sum:int, num_negatives:int) -> int:
    if not node:
        return 0
    cur_sum = cur_sum * 10 + abs(node.val) # 拼接当前值的绝对值
    if node.val < 0: # 累计遇到的负号个数
        num_negatives += 1
    if not node.left and not node.right: # 叶节点 计算符号算正负
        sign = -1 if num_negatives % 2 == 1 else 1
        return cur_sum * sign
    # 递归左右子树
    left_sum = dfs(node.left, cur_sum, num_negatives)
    right_sum = dfs(node.right, cur_sum, num_negatives)
    return left_sum + right_sum