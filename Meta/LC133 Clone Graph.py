from typing import Optional
import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''
1. bfs on OG graph, 过程中copy nodes.用dict{old:new}记录映射关系. dict的key可以当作visted用. 
2. 遍历dict的keys(也就是old nodes) 通过旧节点和邻居的关系 建立新节点和邻居的关系. 
'''
def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None
    queue = collections.deque([node])
    old_to_new = {}
    while queue:
        old = queue.popleft()
        old_to_new[old] = Node(old.val)
        for nei in old.neighbors:
            if nei not in old_to_new:
                queue.append(nei)
    
    for old in old_to_new:
        new = old_to_new[old]
        for nei in old.neighbors:
            new.neighbors.append(old_to_new[nei]) # 注意这里set up新neighbors
    return old_to_new[node]

# Given a ref to a disconnected undirected graph input, return a deep copy.
# Node defined as the above
# 思路与原题一样, 遍历roots里面的每一个root 做原题的逻辑 把新的root append到结果list里.
# T(N + E) S(N) N:total num of nodes, E total num of edges
class Graph:
    def __init__(self, roots:list[Node] = None):
        self.roots = roots

def clone_disconnected_graph(input: Optional['Graph']) -> Optional['Graph']:
    output = Graph([])
    for root in input.roots:
        if not root:
            continue
        # bfs
        queue = collections.deque([root])
        old_to_new = {}
        while queue:
            old = queue.popleft() # 每个节点最多入队/出队一次 一定是没访问过
            old_to_new[old] = Node(old.val)
            for nei in old.neighbors:
                if nei not in old_to_new:
                    queue.append(nei)
        
        for old in old_to_new:
            new = old_to_new[old]
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei]) # 注意这里set up新neighbors
        output.roots.append(old_to_new[root])
    return output    