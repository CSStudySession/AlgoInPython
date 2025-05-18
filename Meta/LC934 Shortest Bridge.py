import collections
'''思路dfs + bfs
1. Find the firstland的初始点 -> fist = (i, j)
2. DFS - Use first to explore Island A and store all land cells in a queue
3. BFS - Find the shortest path from Island A cells -> Island B. 
  -- Only storing water or unvisited cells in our queue
T(n*m) S(n*m) n*m代表节点总个数
'''
def shortestBridge(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    # 1. Find first cell in island A
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                first = (i, j)
                break
    # 2. DFS: find and Load all land cells in island A
    queue = collections.deque()
    dfs(first[0], first[1], queue, grid)
    # 3. BFS: find shortest path from island A cells -> island B
    while queue:
        x, y, dist = queue.popleft()
        for newx, newy in get_nbrs(x, y, grid):
            # Found Island B
            if grid[newx][newy] == 1:
                return dist
            # Found Water
            elif grid[newx][newy] == 0:
                queue.append((newx, newy, dist + 1))
                grid[newx][newy] = -1  # mark as seen
    return -1

def dfs(i, j, queue, grid):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
        queue.append((i, j, 0)) # Load Island A to queue
        grid[i][j] = -1       # mark as seen
        for newx, newy in get_nbrs(i, j, grid):
            dfs(newx, newy, queue, grid)

def get_nbrs(x, y, grid):
    res = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for d in range(4):
        newx = x + dx[d]
        newy = y + dy[d]
        if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]):
            res.append((newx, newy))
    return res