from collections import defaultdict
import heapq
import collections
'''
You are tasked with improving avatar loading times for Roblox experiences
Each avatar is made of multiple components:
(body parts, accessories, animations, etc.)
Some components depend on others - meaning you must load the dependencies firstCompute the correct loading order

Input: [["Head" ]
["Torso"],
["Legs"]]  
output: ["Head","Torso","Legs"]
The first item is the component to load.
The following elements (if any) are dependencies that must be loaded first.
Output:
A list of components, showing the correct loading order:
All dependencies are respected (always load a dependency first)
lf multiple components can be loaded simultaneously, choose based on who appeared earlier in the input list.
lf dependencies are missing (not declared), there is a cycle (dependency loop), or nosolution exists, output ["error!"].

思路:拓扑排序 建图+入度表 用邻接表保存图结构 用in_degree[node]表示一个节点被依赖的次数
输入顺序记录 题目要求在多个节点可同时加载时 选择输入中靠前的
所以记录每个组件首次出现的行列坐标 (row, col) 用于比较优先级

拓扑排序逻辑
使用小顶堆heap 堆中存储 (row, col, node) 自动按输入顺序处理多个入度为0的节点
每处理一个节点 就减少其邻居的入度 如果入度为0 加入堆中
如果存在循环依赖 拓扑排序的结果不会包含全部节点 输出 "error!"
T(nlogn) S(n)
'''
def compute_loading_order(components):
    if not components:
        return []
    graph = defaultdict(list)        # 邻接表
    in_degree = defaultdict(int)     # 入度
    position = collections.defaultdict(tuple)   # 记录每个组件的 (row, col)
    all_nodes = set()

    for row, item in enumerate(components):
        curr = item[0]
        if curr not in position:
            position[curr] = (row, 0)
        all_nodes.add(curr)

        if len(item) > 1:
            dep = item[1]
            graph[dep].append(curr)
            in_degree[curr] += 1
            all_nodes.add(dep)
            if dep not in position:
                position[dep] = (row, 1)  # 出现在后面的位置

    # 入度为0的节点放入堆中，按照行列顺序排序
    heap = []
    for node in all_nodes:
        if in_degree[node] == 0:
            heapq.heappush(heap, (position[node], node))

    result = []
    while heap:
        _, node = heapq.heappop(heap)
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, (position[neighbor], neighbor))

    if len(result) != len(all_nodes):
        return ["error!"]
    return result

input = [
    ['A'],
    ['B'],
    ['C']
]

input = [
    ['A', 'B'],
    ['B', 'C']
]

input = [
    ['A', 'B'],
    ['B', 'A']
]

input = [
    ['A', 'B'],
    ['C', 'B'],
    ['E', 'Q'],
    ['T']
]

print(compute_loading_order(input))