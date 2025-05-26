import collections
'''
dfs:遍历grid 每次遇到1且之前没有search过 就dfs四个方向 dfs过程中求面积 并记录visited. 最后返回一个最大面积
bfs:遍历grid 每次遇到1且之前没有search过 就bfs 每次把周围的unvisited 1入队 bfs过程中求面积 并记录visited 最后返回一个最大面积
T(m*n) S(m*n)
followup: what are some practical limitations of this approach?
- recursion depth limit  - call stack memory usage  - large-scale graphs
'''
def maxArea_dfs(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()
    max_island = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                area = dfs(grid, r, c, visited, rows, cols)
                max_island = max(max_island, area)
    return max_island

def dfs(grid: list[list[int]], r: int, c: int, visited: set[tuple[int, int]], rows: int, cols: int) -> int:
    if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
        return 0

    visited.add((r, c))
    area = 1  # 当前格子计入面积
    # 定义四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        area += dfs(grid, nr, nc, visited, rows, cols)
    return area

# 解法2 bfs.
def maxArea_bfs(grid: list[list[int]]) -> int:
    if not grid:
        return 0
    visited = set()
    maxArea = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
                area = bfs(grid, i, j, visited)
                maxArea = max(maxArea, area)
    return maxArea

def bfs(grid, x, y, visited):
    queue = collections.deque()
    queue.append((x, y))
    area = 0
    while queue:
        x, y = queue.popleft()
        area += 1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited and grid[newx][newy] == 1:
                visited.add((newx, newy))
                queue.append((newx, newy))
    return area