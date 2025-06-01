from typing import List

# 思路: DFS.
# 1. 把图上所有联通区域的面积计算出来 用dict记录
# 2. 遍历grid上每个0 把它变成1 然后四个方向探索是否能与已有的联通区域连接 计算面积
# T(mn), S(mn) from dfs call stack
def largestIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    area = {} # 记录 {联通域_id:对应面积}
    idx = 2   # 给一个区别于0,1的值 用来染色
    ret = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = idx # 染色
                size = dfs(grid, i, j, dx, dy, idx)
                area[idx] = size
                idx += 1
                ret = max(ret, size)
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                cur_max = 1 # 至少有一个'0'可以变1
                # 注意visited在if里面!不能写外面 这里为了防止 当前0把上下左右
                # 本已联通的面积 重复相加. 每个新“0”都单独算自己的
                visited = set()
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != 0 and grid[ni][nj] not in visited:
                        cur_idx = grid[ni][nj]
                        visited.add(cur_idx)
                        cur_max += area[cur_idx]
                ret = max(ret, cur_max)
    return ret

def dfs(self, grid, x, y, dx, dy, idx) -> int:
    cnt = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            grid[nx][ny] = idx
            cnt += self.dfs(grid, nx, ny, dx, dy, idx)
    return cnt


'''
followup: 如果可以flip两个0 怎么解？
1. precompute all connected island areas using DFS and assign each island a unique id.
2. Then for each zero cell, compute its adjacent island set.
3. Next, try flipping two different zero cells, and take the union of their adjacent island ids 
to avoid double-counting areas.
The total size is then the sum of these areas plus 2 for the two flipped zeros.
T(m^2 * n^2)->遍历找成对的0
'''