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
    visited.add((r, c))
    area = 1  # 当前格子计入面积
    # 定义四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 0:
            continue
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
                area = 0
                queue = collections.deque([(i, j)])
                visited.add((i, j))
                while queue:
                    cur = queue.popleft()
                    area += 1
                    dx = [0, 1, 0, -1]
                    dy = [1, 0, -1, 0]
                    for d in range(0, 4):
                        nx = cur[0] + dx[d]
                        ny = cur[1] + dy[d]
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] == 1:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                maxArea = max(maxArea, area)
    return maxArea