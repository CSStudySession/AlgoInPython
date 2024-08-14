'''
https://leetcode.com/company/pinterest/discuss/2881628/Pinterest-or-phone-screen
Given a list of pair of "unrelated images", we need to know whether we can divide the images into two groups
such that no two unrelated images are in the same group.

Case 1
I_1 <-> I_4
I_4 <-> I_8
I_8 <-> I_2

Result:
Group 1 -> [I_1, I_8]
Group 2 -> [I_4, I_2]

Case 2
I_1 <-> I_4
I_4 <-> I_8
I_8 <-> I_1

result: null

思路:
可以将图片视为图中的节点，“不相关的图片对”视为图中的边，
并尝试将图分为两个不包含相邻节点的独立集，这实际上是一个二分图问题。

1.使用BFS遍历图 并同时给每个节点染色:0或1 表示它属于哪个组。
如果在遍历过程中发现一个节点与其相邻节点已经被染成同样的颜色 那么说明无法将图分成两个组 返回None。
2.遍历完所有节点后，根据颜色将节点分成两个组。

时间复杂度
构建图的时间复杂度为O(E) 其中E是边的数量。
BFS遍历的时间复杂度为O(V + E) 其中V是节点数量 E是边的数量。
空间复杂度
图的存储需要O(V + E)的空间。
BFS的队列和颜色标记也需要O(V)的空间。
'''
from typing import List
from collections import deque

def divideImages(pairs: List[List[int]]) -> List[List[str]]:
    # 构建图
    graph = {}
    for a, b in pairs:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    color = {}  # 用于存储每个节点的颜色，0和1代表不同颜色(组)
    for node in graph:
        if node not in color: # 当前点没有被访问过(访问过一定会被染色)
            # 使用BFS
            queue = deque([(node, 0)]) # 从当前点开始做BFS
            color[node] = 0            # 给当前点染色为0
            
            while queue:
                cur_node, cur_clr = queue.popleft()
                for neighbor in graph[cur_node]:
                    if neighbor in color:
                        if color[neighbor] == cur_clr:
                            return None  # 如果相邻的节点有相同的颜色，则不能二分
                    else:
                        color[neighbor] = 1 - cur_clr  # 分配不同的颜色
                        queue.append((neighbor, color[neighbor]))
    
    # 将节点根据颜色分为两组
    group1 = [node for node in color if color[node] == 0]
    group2 = [node for node in color if color[node] == 1]
    
    return [group1, group2]


# unit test case 1
pairs = [["I_1", "I_4"], ["I_4", "I_8"], ["I_8", "I_2"]]
print(divideImages(pairs))  # [['I_1', 'I_8'], ['I_4', 'I_2']]

# Case 2
pairs = [["I_1", "I_4"], ["I_4", "I_8"], ["I_8", "I_1"]]
print(divideImages(pairs))  # None