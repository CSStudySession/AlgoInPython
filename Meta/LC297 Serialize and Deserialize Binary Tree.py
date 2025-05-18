import collections
'''
1.serialize
BFS二叉树逐层
用#表示空节点None 将每个访问到的节点值或#依次加入结果列表
最后去掉列表末尾多余的连续#:不影响结构恢复 并拼成字符串返回
2.deserialize
将序列化得到的字符串去掉外层大括号后按逗号分割 得到字符串数组
先为每个字符创建对应的TreeNode实例 空节点保留#标记
再次BFS 依次为当前节点从数组中取两个元素 分别作为左右子节点 如果不是#就连上并入队 继续下一层构造
T(n), S(n) for both ops
'''
def serialize(root) -> str:
    res = []
    if not root:
        return ""  # 空树直接返回空字符串
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if not node:
            res.append("#")             # 空节点用 "#" 占位
        else:
            res.append(node.val)        # 记录节点值
            queue.append(node.left)     # 左子入队（即使是 None）
            queue.append(node.right)    # 右子入队
    # 去掉末尾多余的"#":最后一层全是# 避免冗余 不影响反序列化
    while res and res[-1] == "#":
        res.pop()
    # 拼接成 "{1,2,3,#,#,4,5}" 形式
    return "{" + ",".join(map(str, res)) + "}"

def deserialize(self, data) -> TreeNode:
    if not data or data == "[]":
        return None                       # 空字符串或空列表格式返回 None
    # 去掉外层大括号，拆分成字符串列表
    data = data[1:-1].split(",")
    # 对应每个字符串都创建一个节点或占位
    nodes = [TreeNode(val) for val in data]
    root = nodes[0]
    queue = collections.deque([nodes[0]])
    i = 1  # 下一个未分配孩子的节点索引
    while queue and i < len(nodes):
        node = queue.popleft()
        # 处理左孩子
        if nodes[i].val != "#":
            node.left = nodes[i]
            queue.append(nodes[i])
        # 否则 left 保持 None
        i += 1 # 注意这里i怎样都会+1 下面处理右孩子的i也是
        # 处理右孩子
        if i < len(nodes) and nodes[i].val != "#":
            node.right = nodes[i]
            queue.append(nodes[i])
        i += 1
    return root