'''
Given an N-ary tree, print the nodes seen by a person when walking from
bottom left to bottom right in an arc via root node.
题目描述故意给的很模糊 只能靠猜+跟对方反复确认理解.
例子1
         1
       / | \
      2  3  4
     / \    / \
    5   6  7   8
输出: [5,2,1,4,8]

例子2:
         1
       / | \
      2  3  4
       \    /
        6  7  
输出:[6,2,1,4,7]

'''
from collections import deque, defaultdict
from typing import List

class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []

def tree_arch_view(root: Node) -> List[int]:
    ret = []
    if not root:
        return ret
    
    map = defaultdict(lambda: [None] * 2) # key是level, value是[0:left_most, 1:right_most] 
    queue = deque([root])
    level = 0

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0: # 当前层的第一个点 是left most node
                map[level][0] = node.val
            if size > 1 and i == size - 1: # 当前层的节点数>1(就一个点的话 肯定是left most) 且当前点是当前层最后一个点: right most node
                map[level][1] = node.val
            for child in node.children:    # 将当前点的所有子节点 从左到右入队
                queue.append(child)
        level += 1 # 注意bfs结束时 level比实际值多加了1
    # print("map:", map)
    # 从左下角开始往上遍历 所以层数倒着数
    for i in range(level - 1, -1, -1): # bfs结束时 level比实际值多加了1 所以从level-1开始倒着遍历
        ret.append(map[i][0])
    # 从第二层开始沿着最右侧往下遍历 第一层的根节点 已在倒着遍历时考虑到了
    for i in range(1, level): 
        if map[i][1]:   # 某一层可能没有right most node  需要判断一下
            ret.append(map[i][1])
    return ret

root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[2].children = [Node(7)]

print(tree_arch_view(root))