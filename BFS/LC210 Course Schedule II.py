'''
https://leetcode.com/problems/course-schedule-ii/description/
返回任意一个拓扑序列 可以用bfs解决
注意: 有向无环图才有拓扑序 有环图一定没有拓扑序
算法框架:
a. 将图中所有入度为零的点入队列  
queue <-- all nodes with in-degree 0
b. 
while queue is not not empty:
  t <- q.front()
  枚举t的所有出边 t <-- j
  删掉出边t->j 并将j的入度减一: in_degree[j] -= 1
  如果in_degree[j] == 0: 将j点入队列 queue <- j
最后队列中的元素顺序 就是一个拓扑序
'''
import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)