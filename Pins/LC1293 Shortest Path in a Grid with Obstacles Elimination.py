'''
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/?envType=company&envId=pinterest&favoriteSlug=pinterest-thirty-days
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

思路: (x,y,z)表示走到(x,y)这个点 消除(走过)了z个障碍物 最少走几步。典型的边权为1的最短路问题 BFS即可
如果允许通过障碍物的个数k很大 通过观察可以得到 其实最多走过m+n-3个障碍物就可以 再大没意义
因为: m+n-1是最短路(横着走再竖着走) 再去掉起始点 中间的格子数为:m+n-1-2==m+n-3 最差情况下每个格子都是障碍物

注意面试时 可能起始点作为输入给出 并不是假设从左上角走到右下角 初始化队列时 把给定的起点入队 出队某个点时 判断是否
为给定的终点.

时间: O(row * col * k) where k is number of obstacles
空间: O(row * col * k)
'''
from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        k = min(k, max(0, row + col - 3)) # 优化时间复杂度
        
        # (x,y,z,step):走到(x,y)点 还能穿过z个障碍物时最小的step
        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])   # 记录走过的状态
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # offset array for BFS
    
        while queue:
            cur_x, cur_y, cur_ob, cur_step = queue.popleft()
            if (cur_x, cur_y) == (row - 1, col - 1): # 走到终点
                return cur_step

            for i in range(4):
                x, y = cur_x + dx[i], cur_y + dy[i]
                if x >= 0 and x < row and y >= 0 and y < col:
                    # (x,y)是obstacle 当前还有消除值可用且该状态没有搜过
                    if grid[x][y] == 1 and cur_ob > 0 and (x, y, cur_ob - 1) not in visited:
                        visited.add((x, y, cur_ob - 1))
                        queue.append((x, y, cur_ob - 1, cur_step + 1))
                    
                    # (x,y)是空地 且该状态没有搜过
                    elif grid[x][y] == 0 and (x, y, cur_ob) not in visited:
                        visited.add((x, y, cur_ob))
                        queue.append((x, y, cur_ob, cur_step + 1))
        return -1  # 注意可能走不到 最后返回-1