'''
Given a binary tree node,return True if every node's value 
is equal to the floor of the average of its descendants (excluding itself).
思路:使用 DFS Post-order Traversal
每个节点从子节点收集:
所有子孙节点的总和 descendant_sum
所有子孙节点的数量 descendant_count
计算该节点是否满足条件:
  - 若descendant_count == 0 跳过检查
  - 否则 检查 node.val == floor(descendant_sum / descendant_count)
用一个全局变量记录是否有节点不满足条件
遍历完整棵树后返回该变量
T(n) S(h) worst n
'''
def isValidAverageTree(root):
    valid = [True]  # 用list封装以便在dfs中修改
    dfs(root, valid)
    return valid[0]

def dfs(node, valid) -> tuple[int, int]:
    if not node:
        return (0, 0)  # sum, count
    # 分别递归左子树和右子树
    left_sum, left_count = dfs(node.left, valid)
    right_sum, right_count = dfs(node.right, valid)
    # 合并子孙信息
    total_sum = left_sum + right_sum
    total_count = left_count + right_count
    # 验证当前节点是否满足题意
    if total_count > 0:
        average = total_sum // total_count
        if node.val != average:
            valid[0] = False
    # 返回包含当前节点在内的总和与个数
    return (total_sum + node.val, total_count + 1)