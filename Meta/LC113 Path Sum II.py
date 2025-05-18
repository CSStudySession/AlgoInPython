'''
1.从根节点开始 维护当前路径path_nodes 和剩余目标和remaining
2.每访问一个节点 就把其值加入当前路径 且remaining-=node.val
 -若到达叶子节点且remaining刚好等于该叶子节点的值 说明找到一条符合目标和的路径 将当前路径拷贝到结果列表中
 -否则分别对左右子树继续递归搜索
3.递归回溯时 将当前节点从路径中弹出 以便探索其他分支
T(n^2):链状树 到叶节点copy路径消耗T(n) S(n):stack + path_list最长n
'''
def pathSum(root: TreeNode, sum: int) -> list[list[int]]:
    res = []
    dfs(root, sum, [], res)
    return res

def dfs(
    node: TreeNode,
    remaining: int,
    path_nodes: list[int],
    path_list: list[list[int]],
) -> None:
    if not node:
        return
    path_nodes.append(node.val)
    if remaining == node.val and not node.left and not node.right:
        path_list.append(path_nodes[:])
    else: # recurse on the left and the right children
        dfs(node.left, remaining - node.val, path_nodes, path_list)
        dfs(node.right, remaining - node.val, path_nodes, path_list)
    # backtrack reset state before dfs
    path_nodes.pop()