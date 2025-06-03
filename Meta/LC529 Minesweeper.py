from collections import deque
'''
BFS
- 从点击点开始遍历。
- 用 queue 存储待处理的格子
- 用 visited 集合避免重复访问。
- 每次出队列时：
  - 统计周围地雷数。
  - 若有地雷：更新当前为数字 然后不拓展邻居！
  - 若无地雷：标记 'B'，继续扩展邻居
T(m*n) S(m*n) -> visited
'''
def updateBoard(board: list[list[str]], click: list[int]) -> list[list[str]]:
    # 如果点击的是地雷，直接结束游戏，标记为 'X'
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
        return board
    # 初始化队列和 visited 集合，避免重复访问
    queue = deque()
    queue.append(click)
    visited = set()
    visited.add(tuple(click))
    while queue:  
        x, y = queue.popleft()
        # 统计当前位置周围地雷数量
        cnt = 0
        neighbors = getNeighbors(x, y, board)   
        for (newx, newy) in neighbors:
            if board[newx][newy] == "M":
                cnt += 1
        if cnt > 0:
            # 周围有雷，显示数字
            board[x][y] = str(cnt)
        else:
            # 周围无雷，标记为 'B'
            board[x][y] = "B"
            # 将所有未访问的邻居加入队列继续扩展
            for (newx, newy) in neighbors:
                if (newx, newy) not in visited and board[newx][newy] == "E":
                    visited.add((newx, newy))
                    queue.append((newx, newy))
    return board

def getNeighbors(self, x, y, board):
    # 获取 (x, y) 周围 8 个方向的合法邻居坐标
    res = []
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    for i in range(8):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < len(board) and 0 <= newy < len(board[0]):
            res.append((newx, newy))
    return res