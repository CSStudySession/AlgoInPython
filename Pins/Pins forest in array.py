'''
给定一个森林结构 它被隐式存储在一个数组中 其中每个节点包含一个parent_index。
实现一个函数 删除指定节点以及它的所有子孙节点(整棵子树) 并消除“碎片化”(deleted标记的节点) 压紧数组 更新父索引
输入：
一个数组forest 每个元素是一个TreeNode对象 包含如下字段:
class TreeNode:
    int parent_index
    bool is_deleted  # 可选字段 用于标记删除
一个整数delete_index 要删除的节点索引
输出:删除指定节点及其子孙后 更新forest的内容 消除碎片 更新parent_index 原地修改(in-place)
约束
如果parent_index==i 说明是根节点. 对所有i, 保证 parent_index <= i(孩子只能在后面)
Clarification
删除节点时，其所有子孙节点都必须被删除。
可以通过增加 is_deleted 字段，或将 parent_index = -1 表示删除。
避免直接移除节点，那是后续 follow-up 的部分。
数据结构是森林（多个树），而不是一棵二叉树。
删除之后，若压缩数组顺序，需要 更新所有 parent_index。
节点没有locality, 5可以在左树 3、4、6 在右树
'''

'''
解法1
从左往右遍历 用集合记录所有要删除的节点
如果某节点的父节点在集合中 则该节点也需要被删除, 标记is_deleted = True
注意:所有节点的parent_index都小于等于自己的索引,因此任何节点的parent一定在它前面或自身(不可能在它后面)
所以 如果当前删除节点的索引是d 那么只有在索引>d的位置 才可能存在以该节点为祖先的节点
T(n) S(n)
'''
def delete_node(forest, delete_index):
    # 标记根节点为删除
    forest[delete_index].is_deleted = True
    deleted_set = set()
    deleted_set.add(delete_index)
    # 遍历后续所有节点
    for i in range(delete_index + 1, len(forest)):
        parent_idx = forest[i].parent_index
        if parent_idx in deleted_set:
            deleted_set.add(i)
            forest[i].is_deleted = True

'''
解法2
1. 遍历forest 建立parent_to_children字典
2. 把delete_index入队 然后开始bfs 每次把children拿出来 用extend入队
T(n) S(n)
'''
from collections import deque, defaultdict
def delete_node_bfs(forest, delete_index):
    # 建立 parent -> children 映射
    parent_to_children = defaultdict(list)
    for i, node in enumerate(forest):
        if i != node.parent_index:  # 不是根节点
            parent_to_children[node.parent_index].append(i)
    # BFS 删除
    queue = deque()
    queue.append(delete_index)
    while queue:
        curr = queue.popleft()
        forest[curr].is_deleted = True
        queue.extend(parent_to_children[curr]) # 注意一定要extend()

'''
解法3
从右向左遍历, 对每个未处理节点，沿着 parent 指针回溯，直到找到根或发现祖先被删除
如果有祖先被删，则整个链都标记删除
T(n^2) S(h) h is tree height, worst n.
'''
def delete_node_reverse(forest, delete_index):
    forest[delete_index].is_deleted = True
    n = len(forest)

    def has_deleted_ancestor(i):
        while forest[i].parent_index != i:
            i = forest[i].parent_index
            if forest[i].is_deleted:
                return True
        return False

    for i in range(n - 1, -1, -1):
        if not forest[i].is_deleted and has_deleted_ancestor(i):
            forest[i].is_deleted = True

'''
followup:in-place的删除已经mark为deleted的节点 并更新parent index
思路: 使用fast指针遍历原始森林, slow指针记录下一个未删除节点应该放置的位置 实现in-place update
用一个old_to_new字典记录每个原始节点位置被移动到的新位置
在每次移动一个节点后 立即修正它的parent_index 把原parent的位置用old_to_new进行映射
最后通过切片forest[:] = forest[:slow]截断删除多余的尾部节点
T(n) S(n)
'''
# 找到index对应节点的old parent,如果它之前被搬家了 就找到它的新位置
# 如果没有 返回自己(代表还没搬家)
def get_updated_parent(forest, old_to_new, index):
    old_parent = forest[index].parent_index
    return old_to_new.get(old_parent, old_parent)

def reduce_fragmentation(forest):
    old_to_new = dict()
    slow = 0
    for fast in range(len(forest)):
        if forest[fast].is_deleted == True: # 跳过被标记为deleted的节点
            continue
        forest[slow] = forest[fast] # copy node
        # update parent
        forest[slow].parent_index = get_updated_parent(forest, old_to_new, fast)
        # 原来在fast位置的节点 现在被放到了slow这个位置 为了后面更新parent_index使用
        old_to_new[fast] = slow
        slow += 1
    forest[:] = forest[:slow]  # truncate util (slow - 1)