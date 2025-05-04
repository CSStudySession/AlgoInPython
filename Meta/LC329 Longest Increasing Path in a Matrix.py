'''
variant: you can traverse only if the number is consecutively increasing like 1->2->3->4
思路:dfs+记忆化搜索.
T(m*n) S(m*n)
'''
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    ret = 0
    memo = {}
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ret = max(ret, dfs(i, j, memo, direction, matrix))
    return ret

def dfs(x, y, memo, direction, matrix) -> int:
    if (x, y) in memo:
        return memo[(x, y)]
    
    length = 1
    for k in range(4):
        nx = x + direction[k][0]
        ny = y + direction[k][1]
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == matrix[x][y] + 1: # 这里限制了只能连续递增
            length = max(length, dfs(nx, ny, memo, direction, matrix) + 1)
    memo[(x, y)] = length
    return length

# OG. dfs+记忆化搜索
def longestIncreasingPath(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    ret = 0
    memo = {}
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ret = max(ret, dfs(i, j, memo, direction, matrix))
    return ret

def dfs(x, y, memo, direction, matrix) -> int:
    if (x, y) in memo:
        return memo[(x, y)]
    
    length = 1 # 每次dfs要初始化length 当前cell起码算一个length 故为1
    for k in range(4):
        nx = x + direction[k][0]
        ny = y + direction[k][1]
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
            # 注意取max的写法
            length = max(length, dfs(nx, ny, memo, direction, matrix) + 1)
    memo[(x, y)] = length
    return length