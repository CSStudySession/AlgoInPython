
'''

'''
from typing import List
import collections


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = collections.defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()
        return self.dfs(0, adjList, visited, hasApple) * 2
    
    def dfs(self, cur_node: int, graph: dict[int, List[int]], visited: set[int], hasApple: List[bool]) -> int:
        step = 0
        for nbr in graph[cur_node]:
            if not nbr in visited:
                visited.add(cur_node)
                step += self.dfs(nbr, graph, visited, hasApple)
                visited.remove(cur_node)
        if (hasApple[cur_node] or step != 0) and cur_node != 0:
            step += 1
        return step
