from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid) - 1
        if grid[0][0] == 1 or grid[size][size] == 1: return -1
        if len(grid) == 1: return 1

        queue, level = deque([(0,0)]), 2 # at least two cells: start and end cells
        while queue:
            for _ in range(len(queue)):
                coord_y, coord_x = queue.popleft()
                for (dx,dy) in ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)):
                    nx, ny = coord_x + dx, coord_y + dy
                    if nx < 0 or ny < 0 or nx > size or ny > size or grid[ny][nx] != 0: # filter out unfeasible cell
                        continue
                    if ny == size and nx == size: # find end cell
                        return level
                    grid[ny][nx] = 2 # act as a visted set
                    queue.append((ny, nx)) # enqueue a feasible new cell
            level += 1
        return -1 