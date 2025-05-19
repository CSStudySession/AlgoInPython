import collections
'''
思路:dfs 目标是最小化采集所有苹果所需的总路径长度。
- 建图：用邻接表构建树的结构（无向图）。
- DFS 遍历 从根节点 0 开始，递归地访问子节点。
- 路径计数：若某子树中有苹果（包括当前节点），则说明我们需要“去+回”这条路径，贡献时间 2。
- 返回总步数x2 因每条边走两次 最终乘以2得到总时间
T(n) s(n)
'''
def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
    adjList = collections.defaultdict(list)
    for edge in edges: # 无向图建adj list
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    visited = set([0]) # 从0号根节点出发
    return dfs(0, adjList, visited, hasApple) * 2 # 去和回两趟 步数*2

def dfs(cur_node: int, graph: dict[int, list[int]], visited: set[int], hasApple: list[bool]) -> int:
    step = 0
    for nbr in graph[cur_node]:
        if not nbr in visited:
            visited.add(nbr)
            step += dfs(nbr, graph, visited, hasApple)
            visited.remove(nbr)
    # 当前节点自己有苹果 或者它的子树中有苹果(step!=0) 且它不是根节点 路径回传时+1再返回给上层调用
    if (hasApple[cur_node] or step != 0) and cur_node != 0:
        step += 1
    return step
