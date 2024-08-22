'''
https://www.1point3acres.com/bbs/thread-812296-1-1.html
一个m*n的矩阵
0表示可走 1表示墙 求从a到b的最短路径
变种题1: v1
array里有大小写字母 A B C ...表示门, a b c...表示钥匙 有钥匙才能过门
变种题2: v2
中间有墙和不同的门， 墙过不去，门需要用特定的钥匙打开 matrix只有一个门的钥匙

思路:BFS遍历 在每一轮BFS中 从队列中取出当前的位置、当前收集到的钥匙状态和当前步数。
对当前点的四个方向进行扩展：
- 如果是墙 '1'，跳过。
- 如果是钥匙（小写字母），更新钥匙的状态。
- 如果是锁（大写字母），检查是否有对应的钥匙，有则继续，否则跳过。
- 对于空地 '0'，直接继续搜索。
- 每走一步后，将新状态加入队列，并将状态标记为已访问。
终止条件 一旦达到终点 返回当前步数 如果队列为空但仍未达到目标状态 返回-1表示无法到达终点

时间复杂度分析
状态数：由于有 k 把钥匙，钥匙的状态可以用 2^k 表示，而每个位置 (i, j) 可能有 2^k 种状态。
BFS遍历 队列中最多会有 O(m * n * 2^k) 个状态，每个状态最多有 4 个扩展方向。
因此，时间复杂度为 O(m * n * 2^k * 4)，即 O(m * n * 2^k)。

空间复杂度分析
队列空间：最多会有 O(m * n * 2^k) 个状态在队列中。
访问标记：同样需要 O(m * n * 2^k) 的空间来存储访问过的状态。
因此，空间复杂度也是 O(m * n * 2^k)
'''
from typing import List
from collections import deque

def shortest_path_v1(grid: List[List[str]], start: List[int], end:List[int]) -> int:
    if not grid or not grid[0] or (grid[end[0]][end[1]] == '1'):
        return -1
    
    row, col = len(grid), len(grid[0])
    
    # 注意如果Bfs目标是走到终点 则不需要统计总共的钥匙数量
    # 遍历grid 收集所有钥匙数
    # for i in range(row):
    #    for j in range(col):
    #        if grid[i][j].isalpha() and grid[i][j].islower(): # 钥匙
    #            key += 1
    
    # BFS准备
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set([(start[0], start[1], 0)])
    
    # BFS中的offset
    dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
    while queue:
        cur_x, cur_y, cur_key, cur_dist = queue.popleft()
        if cur_x == end[0] and cur_y == end[1]:
            return cur_dist
        
        for i in range(4):
            x, y = cur_x + dx[i], cur_y + dy[i]
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == '1':
                continue
            char = grid[x][y]
            if char >= 'a' and char <= 'z':     # 小写字母代表钥匙
                nxt_key = cur_key | 1 << (ord(char) - ord('a'))
                if (x, y, nxt_key) not in visited:
                    queue.append((x, y, nxt_key, cur_dist + 1))
                    visited.add((x, y, nxt_key))
            elif char >= 'A' and char <= 'Z':  # 大写字母代表门 需要判断是否有对应的钥匙
                pos = ord(char) - ord('A')
                if (cur_key >> pos) & 1 and (x, y, cur_key) not in visited:
                    queue.append((x, y, cur_key, cur_dist + 1))
                    visited.add((x, y, cur_key))
            else: # '0'代表空地
                if (x, y, cur_key) not in visited:
                    visited.add((x, y, cur_key))
                    queue.append((x, y, cur_key, cur_dist + 1))
    
    return -1

# unit test
grid1 = [
    ['0', '0', '0', '0'],
    ['0', 'a', '1', 'B'],
    ['0', 'A', 'b', '0'],
    ['0', '0', '0', '0']
]
start1 = [0, 0]
end1 = [3, 3]
print(shortest_path_v1(grid1, start1, end1))

grid2 = [
    ['0', '1', '0', '0'],
    ['0', '1', 'B', '0'],
    ['0', 'a', '1', '0'],
    ['0', 'A', '0', '0']
]
start2 = [0, 0]
end2 = [3, 3]
print(shortest_path_v1(grid2, start2, end2))