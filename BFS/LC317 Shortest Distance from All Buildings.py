'''
https://leetcode.com/problems/shortest-distance-from-all-buildings/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

'''

from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist, cnt = defaultdict(int), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, m, n, i, j, cnt, dist)
                    cnt += 1
        min_dist = float("inf")
        for (x, y), step in dist.items():
            if grid[x][y] == -cnt:
                min_dist = min(min_dist, step)
        return min_dist if min_dist != float("inf") else -1

    def bfs(self, grid, m, n, i, j, cnt, dist):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(0, i, j)])
        while queue:
            step, x, y = queue.popleft()
            step += 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == -cnt:
                    queue.append((step, nx, ny))
                    grid[nx][ny] -= 1
                    dist[(nx, ny)] += step