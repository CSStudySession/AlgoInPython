'''
given the root of a binary tree where every non-leaf node's value is defined
as the boolean AND of its children. In other words,
for any non-leaf node:node.value = node.left.value & node.right.value 
Each leaf node has a value of either 0 or 1. 
It is guaranteed that the input tree is valid. 
You are also given a pointer to one of the leaf nodes in the tree. 
Your task is to flip the value of that leaf node (change 0 to 1 or 1 to 0),
and update the tree along the unique path from that leaf back to the root,
so that the boolean AND property is maintained for every non-leaf node.
Example1
Input:
       0
      / \
     0   1
    / \
   1  0
Leaf to flip: The right child of the left node (value 0).
Explanation:
- Initially, the left node's value is 1 AND 0 = 0.
- After flipping the leaf from 0 to 1, its parent's new value becomes 1 AND 1 = 1.
- Update the root: new root value = 1 AND 1 = 1.
Output:
       1
      / \
     1   1
    / \
   1   1
note:
Ask if we are given parent pointers. If we are, we can simply do a leaf to root traversal. 
If the parent's value remains unchanged, we can stop early.
'''
'''
假设有parent pointer. 先改变给定leaf的值 然后沿parent pointer一路更新.
'''
def flip_and_update(leaf: TreeNode) -> None:
    # 第一步：翻转叶子节点的值
    leaf.val = 1 - leaf.val  # 0 -> 1, 1 -> 0

    # 第二步：从叶子节点向上更新祖先节点的值
    node = leaf.parent
    while node:
        old_val = node.val
        # 使用左右子节点的值重新计算
        node.val = node.left.val & node.right.val
        # 如果值没变，可以提前结束
        if node.val == old_val:
            break
        node = node.parent

'''
如果没有parent pointer. dfs构建root-to-leaf path.
从倒数第二个节点(leaf的parent)开始往前遍历 修改每个node的val.
T(n) S(n)
'''
def find_and_flip(root: TreeNode, leaf: TreeNode) -> None:
    if not leaf:
        return
    path = []
    find_path_to_leaf(root, leaf, path) # dfs构建root到leaf的path

    leaf.val = 1 - leaf.val # 更改leaf的值
    for i in range(len(path) - 2, -1, -1): # 倒数第二个元素开始 最后一个是leaf
        old_val = path[i].val
        path[i].val = path[i].left.val & path[i].right.val # 根据定义更新值
        if old_val == path[i].val: # 当值不变时 可提前break
            break 
def find_path_to_leaf(node, leaf, path) -> bool: # 返回leaf是否在以node为根的树中 并收集node到leaf路径
    if not node:
        return False
    path.append(node)
    if node is leaf: # 注意判断当前点如果是leaf 即可返回
        return True
    if find_path_to_leaf(node.left) or find_path_to_leaf(node.right):
        return True
    path.pop() # 注意要pop
    return False