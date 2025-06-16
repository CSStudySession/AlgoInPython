'''
输入是一个 M x N 的二值矩阵：
0 表示该格子为空地（可通行）
1 表示墙（不可通行，除非使用炸弹）
起点是左上角 (0, 0)，终点是右下角 (M-1, N-1)。
机器人每次可以向 4 个方向移动（上、下、左、右）。
机器人有 K 个炸弹，每个炸弹可以将一个 1 变为 0。
'''

'''
part 1:
输入:一个二维整数数组 matrix, 一个整数 K(表示炸弹数量)
输出: bool 机器人能否从起点走到终点?
思路: DFS + backtracking(带炸弹数量状态)
在DFS中加入剩余炸弹数作为状态的一部分 同时记录visited状态避免重复访问无意义路径。
如果状态(x, y, bombs_left)访问过 则直接返回False (之前访问的时候没有返回True)
T(M*N*K) k is # of bomb, S(m*n*k) for visited
'''
def can_reach_target(grid, k_bomb):
    if not grid or not grid[0]:
        return False

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(x, y, bombs_left):
        # 如果越界或访问过同状态
        if x < 0 or x >= rows or y < 0 or y >= cols or (x, y, bombs_left) in visited:
            return False

        # 终点
        if x == rows - 1 and y == cols - 1:
            if grid[x][y] == 0 or bombs_left > 0:
                return True
            else:
                return False

        # 处理墙
        if grid[x][y] == 1:
            if bombs_left == 0:
                return False
            bombs_left -= 1  # 炸掉这堵墙
        visited.add((x, y, bombs_left))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if dfs(x + dx, y + dy, bombs_left):
                return True
        return False
    return dfs(0, 0, k_bomb)

'''
part 2: 如果bomb数量>1? 把bomb数量当成一个dfs参数, part 1的code里已经实现了.
'''

'''
part3: any heuristic way to optimize? 
每个 (i, j) 最多记录一条“最优路径”状态（即剩余炸弹数最大的）
如果当前状态炸弹数少于记录的最大值，就剪枝，不继续递归
最差的时间复杂度仍是T(m*n*k) 空间复杂度成:S(m*n)
'''
def can_reach_target(grid, k_bomb):
    if not grid or not grid[0]:
        return False

    rows, cols = len(grid), len(grid[0])
    visited_bomb_left = {}

    def dfs(x, y, bombs_left):
        # 越界
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False

        # 剪枝：之前到达这个点时炸弹更多，当前这条路径更差
        if (x, y) in visited_bomb_left and visited_bomb_left[(x, y)] >= bombs_left:
            return False
        visited_bomb_left[(x, y)] = bombs_left

        # 终点
        if x == rows - 1 and y == cols - 1:
            if grid[x][y] == 0 or bombs_left > 0:
                return True
            else:
                return False

        # 遇到墙，尝试用炸弹
        if grid[x][y] == 1:
            if bombs_left == 0:
                return False
            bombs_left -= 1

        # 四个方向继续DFS
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if dfs(x + dx, y + dy, bombs_left):
                return True

        return False

    return dfs(0, 0, k_bomb)