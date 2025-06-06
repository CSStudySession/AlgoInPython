from collections import deque
'''
bfs
定义四个方向（上下左右）作为搜索方向。
每次从队列中取出当前节点 (x, y)，判断是否为目标点。
对于每个方向 (dx, dy)，从当前点出发沿该方向一直滚动，直到撞到墙或边界。
滚动结束后的位置 (nx, ny) 是一个转弯点，如果该位置没有访问过，就将其加入队列和 visited。
注意我们只记录转弯点，不需要记录中间经过的位置，因为球经过中间不会停留，也不会在中途转弯。
say maze is m*n 每个点最多入队列一次 每个节点最多尝试4个方向 每个方向最多滚动max(m,n)步
T(m*n * max(m,n))  S(m*n)
'''
def hasPath(maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
    queue = deque()
    queue.append((start[0], start[1]))
    visited = set()
    visited.add((start[0], start[1]))
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y = queue.popleft()
        if [x, y] == destination:
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 一直走 直到撞墙或者出界
            while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                nx += dx
                ny += dy
            # 退回多走的一步
            nx -= dx
            ny -= dy
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False