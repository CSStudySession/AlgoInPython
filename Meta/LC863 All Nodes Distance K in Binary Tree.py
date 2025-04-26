import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
1. 需要bfs来一层层往外拓展 由于没有parent信息 需要先遍历树 过程中记录每个node的parent
2. 从target开始bfs 记录visted nodes. 每个节点的左右node和parent 没visted的入队
3. 当step==k时 结束bfs. 此时队列中存在的nodes即为答案. 注意不能bfs的过程中就把node加入结果.
'''
def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    if not root:
        return []
    parent = {}
    build_parent(root, parent)
    queue = collections.deque([target])
    step = 0
    visited = {target} # set对象初始化用花括号 不能set(x)!

    while queue and step < k: # 注意<k! step从0开始就执行bfs逻辑了
        for _ in range(len(queue)): # 注意这里要再for 遍历当前层
            curr = queue.popleft()
            if curr.left and curr.left not in visited: # 判断没有visit过
                queue.append(curr.left)
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                queue.append(curr.right)
                visited.add(curr.right)
            if curr in parent and parent[curr] not in visited:
                queue.append(parent[curr])
                visited.add(parent[curr])
        step += 1 # 该层遍历完了再step += 1
    return [node.val for node in queue] # 注意写法

def build_parent(node, parent):
    if not node:
        return
    if node.left:
        parent[node.left] = node
    if node.right:
        parent[node.right] = node
    build_parent(node.left, parent)
    build_parent(node.right, parent)