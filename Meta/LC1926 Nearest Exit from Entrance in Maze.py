import collections
'''
思路:BFS.从入口开始做BFS搜索 按层扩展四个方向
每访问一个空格就标记为已访问(in-place修改matrix节省空间)
直到遇到边界上的非入口空格 返回对应步数
T(m*n) S(m*n):队列容量
'''
def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    rows, cols = len(maze), len(maze[0])
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    start_row, start_col = entrance
    
    maze[start_row][start_col] = "+"
    
    queue = collections.deque()
    queue.append([start_row, start_col, 0])
    while queue:
        cur_row, cur_col, curr_distance = queue.popleft()
        # 注意特判不等于入口->cur_dis>0
        if (cur_row == 0 or cur_row == rows - 1 or cur_col == 0 or cur_col == cols - 1) and curr_distance != 0:
            return curr_distance
        for d in dirs:
            next_row = cur_row + d[0]
            next_col = cur_col + d[1]
            if 0 <= next_row < rows and 0 <= next_col < cols \
                and maze[next_row][next_col] == ".":
                maze[next_row][next_col] = "+" # in-place update
                queue.append([next_row, next_col, curr_distance + 1])
    return -1
