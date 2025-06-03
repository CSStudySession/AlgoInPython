from collections import deque
'''
multi-source bfs. 
- 初始化队列
遍历整个房间矩阵，把所有门的位置加入队列，作为 BFS 的起点。
-BFS
每次从队列中取出一个位置 (x, y)，尝试向四个方向扩展。对于每一个邻居 (newx, newy):
如果是空房间（即当前值比 rooms[x][y] + 1 大）说明我们找到了更短路径 就更新它的值为 rooms[x][y] + 1 并加入队列继续扩展
- 终止条件：
队列为空时BFS结束 由于是从所有门同时开始扩展的 所以保证了每个空房间被第一次访问时即为其最短路径
T(m*n) S(m*n)
'''
def wallsAndGates(rooms: list[list[int]]) -> None:
    queue = deque()
    if not rooms: return 
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == 0:
                queue.append((i, j)) # multi-source BFS
    while queue:
        x, y = queue.popleft()
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < len(rooms) and 0 <= newy < len(rooms[0]) and rooms[newx][newy] > rooms[x][y] + 1:
                rooms[newx][newy] = rooms[x][y] + 1
                queue.append((newx, newy))
