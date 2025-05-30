from collections import deque
'''
dfs or bfs通用思路 遍历二维矩阵
每当遇到一个 '1' 就从该点出发 通过DFS或BFS 每次新发现一个未访问的 '1' 就代表找到了一个新的岛屿 更新岛屿数
将与其相连的所有 '1' 标记为 '0'（表示已访问)
'''
# T(m*n) S(min(m, n))
def numIslands_BFS(grid: list) -> int:
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1  # 发现一个新岛屿
                queue = deque()
                queue.append((i, j))
                grid[i][j] = '0'  # 标记为访问过

                while queue:
                    x, y = queue.popleft()
                    # 检查四个方向
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = x + dx
                        ny = y + dy
                        # 边界判断 + 未访问判断
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'  # 标记访问
                            queue.append((nx, ny))
    return count

# T(m*n) S(m*n)
def numIslands_DFS(grid: list) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)
    return count

def dfs(grid: list, r: int, c: int):
    rows = len(grid)
    cols = len(grid[0])
    # 边界或水则返回
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
        return

    grid[r][c] = '0'  # 标记为访问过
    # 递归四个方向
    dfs(grid, r + 1, c)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)
    dfs(grid, r, c - 1)