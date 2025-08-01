from typing import List, collections

# leetcode OG bfs. 直接修改输入 优化空间复杂度. T(m*n) S(n*n) 每个格子最多处理1次
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    size = len(grid) - 1
    if grid[0][0] == 1 or grid[size][size] == 1:
        return -1
    if len(grid) == 1: # n * n 只有1个格子
        return 1
    
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    step = 0
    queue = collections.deque([(0,0)])
    grid[0][0] = 1 # 把走过的路变成obsticles 节省用visited
    while queue:
        step += 1 # 这里加step 之后不用加了
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == size and y == size:
                return step
            for d in range(8):
                newx = x + dx[d]
                newy = y + dy[d]
                if 0 <= newx <= size and 0 <= newy <= size and grid[newx][newy] == 0:
                    queue.append((newx, newy))
                    grid[newx][newy] = 1 # mark visited
    return -1

# variant1: return one shorest path. 
# 解法1: bfs的过程中 用dict[(nx, ny)] = (x, y)表示从(x,y)走到的(nx,ny). 在终点back trace回去.
def oneShortestPathBinaryMatrix(grid: List[List[int]]) -> List[tuple[int]]:
    size = len(grid) - 1
    if grid[0][0] == 1 or grid[size][size] == 1:
        return []
    if len(grid) == 1: # n * n 只有1个格子
        return [(0, 0)]
    
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    queue = collections.deque([(0,0)])
    trace = collections.defaultdict(tuple)
    grid[0][0] = 1 # 把走过的路变成obsticles 节省用visited
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == size and y == size:
                ret = collections.deque()
                ret.appendleft((x, y))
                while (x, y) != (0 ,0):
                    (x, y) = trace[(x, y)]
                    ret.appendleft((x, y))
                return list(ret)
            for d in range(8):
                newx = x + dx[d]
                newy = y + dy[d]
                if 0 <= newx <= size and 0 <= newy <= size and grid[newx][newy] == 0:
                    queue.append((newx, newy))
                    trace[(newx, newy)] = (x, y)
                    grid[newx][newy] = 1 # mark visited
    return []

grid0 = [[0,0,0],[1,1,0],[1,1,0]]
grid1 = [[0,1],[1,0]]
print(oneShortestPathBinaryMatrix(grid0))

# variant1: return one shorest path. 
# 解法2: bfs的queue中 每个元素(x,y, path_so_far) path_so_far为起点到当前点的路径
# 这样空间复杂度与bfs一样
def one_shortest_path(grid: List[List[int]]) -> List[tuple[int]]:
    size = len(grid) - 1
    if grid[0][0] == 1 or grid[size][size] == 1:
        return []
    if len(grid) == 1: # n * n 只有1个格子
        return [(0, 0)]
    
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    queue = collections.deque([(0, 0, [(0,0)])])
    grid[0][0] = 1 # 把走过的路变成obsticles 节省用visited
    while queue:
        for _ in range(len(queue)):
            x, y, path = queue.popleft()
            if x == size and y == size:
                return path
            for d in range(8):
                newx = x + dx[d]
                newy = y + dy[d]
                if 0 <= newx <= size and 0 <= newy <= size and grid[newx][newy] == 0:
                    queue.append((newx, newy, path + [(newx, newy)])) # 注意不能用extend()
                    grid[newx][newy] = 1 # mark visited
    return []

# variant2: return any one path, not necessary shorest.
# DFS返回任意一条path. 由于每个cell只会被访问1次 这里不需要回溯时候reset grid visited status
# T(m*n) S(m*n)
def onePathBinaryMatrix(grid: List[List[int]]) -> List[tuple[int]]:
    if not grid or grid[0][0] != 0 or grid[len(grid) - 1][len(grid[0]) - 1] != 0:
        return []
    tmp = [(0,0)]
    ret = []
    grid[0][0] = 1
    dfs(ret, tmp, grid, 0, 0)
    return ret
    
def dfs(ret, tmp, grid, x, y):
    if len(ret) > 0: # 找到一个解
        return True
    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        ret.append(tmp[:]) # 这里要深拷贝
        return True
    
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, 1, -1]
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= len(grid) - 1 and 0 <= ny <= len(grid[0]) - 1 and grid[nx][ny] == 0:
            grid[nx][ny] = 1 # mark visted
            tmp.append((nx, ny)) # add trace
            if dfs(ret, tmp, grid, nx, ny):
                return True
            tmp.pop()  # restore tmp path status. 注意不要reset grid访问状态 每个状态只需要被访问到一次
    return False

grid0 = [[0,0,0],[1,1,0],[1,1,0]]
grid1 = [[0,1],[1,0]]
print(onePathBinaryMatrix(grid0))

'''
some followups:
- 如果要求路径必须经过坐标 (a, b)?
可拆分成两段BFS (0, 0) → (a, b) 和 (a, b) → (m - 1, n - 1)
两次BFS之间要还原被修改过的grid 或给每次BFS都用一个新的visited数组 避免互相干扰
- 如果有k个必经坐标?
1. 如果访问顺序已经给定 即必须按照顺序经过k个点
把起点—> point 1, point 1 -> point 2 ... 做k+1次bfs 最后累加长度.
2. 如果访问顺序不确定 自己挑顺序使得整条路最短
NP-hard问题.枚举k!种顺序 对每个顺序做k+1次BFS 选最小值
'''

'''
variant3: return the number of possible unique paths -> leetcode 63
that the you can take to reach the bottom-right corner. 返回路径数量 图中可能有障碍
note you can only move 4 directors, and either move down or right
思路: dfs + memo
利用 DFS 遍历所有可能路径, 用 memo 记忆子问题结果，避免重复计算；
每次到达终点计为一条路径；
用 grid[x][y]=2 临时标记当前路径，防止重复访问；
回溯时恢复状态，保证其他路径可访问。
T(m*n) S(m*n)
'''
def calc_number_of_path(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    def dfs(x, y, grid, memo):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y]==1 or grid[x][y]==2:
            return 0
        if x == m - 1 and y == n - 1:
            return 1  # 意思是当前这条路径 算1条可行路径 不用考虑从哪个方向来的 下面dfs考虑
        if (x,y) in memo:
            return memo[(x,y)]
        memo[(x,y)] = 0
        grid[x][y] = 2  # 注意这里要set一个值 为了防止当前的dfs走回头路
        memo[(x,y)] += dfs(x + 1, y, grid, memo)
        memo[(x,y)] += dfs(x , y + 1,grid, memo)
        grid[x][y] = 0 # dfs完了reset 该点可能在其他路径上也会用到
        return memo[(x,y)]
    return dfs(0, 0, grid, {})