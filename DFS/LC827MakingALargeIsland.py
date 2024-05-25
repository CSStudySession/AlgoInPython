from typing import List
from typing import Dict

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        area: Dict[int, int] = {} # area[island_id] = area, island_id is the key
        res = 0
        index = 2
        size = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = index
                    size = self.dfs(i, j, grid, index) 
                    area[index]  = size
                    res = max(res, area[index])
                    index += 1
      

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0: # 遍历所有0 尝试变成1之后计算连起来的area
                    maxArea = 1
                    visited = set()     # island_id
                    for (newi, newj) in self.getNeighbors(i, j):
                        if self.isValid(newi, newj, grid) and grid[newi][newj] not in visited and grid[newi][newj] in area:
                            visited.add(grid[newi][newj])
                            island_id = grid[newi][newj]
                            maxArea += area[island_id]
                    res = max(res, maxArea) # 注意res位置 需要对每一个0更新面积
        return res

    def dfs(self, x, y, grid, index) -> int:
        count = 1
        for (newx, newy) in self.getNeighbors(x, y):
            if self.isValid(newx, newy, grid) and grid[newx][newy] == 1:
                grid[newx][newy] = index
                count += self.dfs(newx, newy, grid, index)
        return count
    
    def getNeighbors(self, x, y) -> List[int]:
        res = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            res.append((newx, newy))
        return res
    
    def isValid(self, x, y, grid) -> bool:
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])