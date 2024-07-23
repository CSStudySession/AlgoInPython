'''
same set up as https://leetcode.com/problems/course-schedule-ii/
it requries to return all topological sort
1. 根据边与边的关系 建立有向图 注意边的指向
2. 建图过程中 构建in_degree数组:in_degree[i]代表i号点的入度
3. dfs找所有的path dfs过程如下
a. 遍历所有的点 如果当前点x满足如下条件:
    - 入度为0: in_degree[x] == 0
    - 没有在当前的路径上遍历过 visited[x] == False
    将该点放入探索路径上 tmp.append(x)
b. 记录当前点x为visited 并把它的出边的所有入度都减1(in_degree[i] -= 1 for all x->i)
c. 递归调用dfs
d. dfs调用返回 还原所有状态:
   - 还原x的出边点所有的入度(in_degree[i] += 1 for all x->i)
   - 当前探索路径上删掉x: tmp.pop()
   - 当前点x记录为un-visited

Time Complexity: O(V!) V is the number of vertices, V! is absolute worst case. 
(worst case example: any graph with no edges at all)
Space: O(V) for creating an additional array and recursive stack space.
'''
from typing import List
import collections

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = collections.defaultdict(list)
    in_degree = [0] * numCourses
    res = []
    visited = [False] * numCourses
    for x, y in prerequisites:
        graph[y].append(x)
        in_degree[x] += 1
    find_all_topo_orders(res, graph, in_degree, [], numCourses, visited)
    return res

def find_all_topo_orders(res, graph, in_degree, tmp, n, visited):
    if len(tmp) == n:
        print("found one:", tmp)
        res.append(tmp[:])
        return
    
    for vtx in range(n):
        if in_degree[vtx] == 0 and not visited[vtx]:
            visited[vtx] = True
            tmp.append(vtx)
            for nei in graph[vtx]:
                in_degree[nei] -= 1
            find_all_topo_orders(res, graph, in_degree, tmp, n, visited)
            for nei in graph[vtx]:
                in_degree[nei] += 1
            tmp.pop()
            visited[vtx] = False

n = 4
p = [[1,0], [2,0], [3,2], [3,1]]
n = 3
# p = [[1,0], [2,1], [0,2]]
print(findOrder(n, p))
