'''
variant: mouse and cheese. mouse置于一个mase with unknown dimensions m*n, starting at [0,0]
return True if we can find cheese.
given API: move(direction), has_cheese()
思路与OG相同 区别:
1. 不需要手动turnRight() move()可以通过传入方向和(i,j)判断是否可以走
2. 如果不能走 即move()返回False 题目要求要手动退回来一步.所以要有两个方向数组(dir和reverse_dir)
T(m*n) S(m*n)
'''
class Mouse:
    def __init__(self):
        pass
    # The move(Direction) will move the mouse regardless of whether you can or not
    def move(self, direction, i, j) -> bool:
        pass
    def has_cheese(self, i, j) -> bool:
        pass

    def find_cheese(self) -> bool:
        visited = set([(0,0)])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        reverse_directions = [(1,0), (0,-1), (-1,0), (0,1)]
        return self.dfs(0,0, directions, reverse_directions, visited)
    
    def dfs(self, i, j, directions, reverse_directions, visited) -> bool:
        if self.has_cheese(i, j):
            return True
        visited.add((i, j)) # 进入dfs先add visited
        for k in range(directions):
            ni = i + directions[k][0]
            nj = j + directions[k][1]
            if (ni, nj) in visited:
                continue
            if not self.move(directions[k], i, j): # 不能走的格子 要手动退回来
                self.move(reverse_directions[k], i, j)
                continue
            if self.dfs(ni, nj, directions, reverse_directions, visited):
                return True
            self.move(reverse_directions[k], i, j) # dfs后回溯一步
            # 注意不需要set.remove()我们只要cell被访问到即可 不关心具体访问路径
        return False # 前面都没return 最后要return False

'''
OG 思路: DFS + 回溯
- 把机器人当前所在位置看作 (0,0)，然后用 DFS 向四个方向探索。
- 每走到一个新位置就调用 clean() 清洁，然后继续向未知方向搜索。
  -- 如果某个方向 move() 返回 False 说明撞墙 不能走 就尝试下一个方向。
  -- 如果走成功 递归进入下一个格子 clean完后回退:goBack()到原来的位置 继续探索其他方向。
  -- 用一个 visited 集合记录清扫过的坐标，防止重复清洁。
- 方向控制
  -- 用一个directions [(-1,0), (0,1), (1,0), (0,-1)] 表示上、右、下、左的四个方向。
初始时机器人朝“上”（(-1, 0)），每次 turnRight() 会让机器人顺时针旋转 90 度。
T(m*n) S(m*n)
'''
class Solution:
    def cleanRoom(self, robot) -> None:
        if not robot:
            return
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # 要按顺时针有序定义
        direction = 0  # 初始状态冲上:(-1, 0)
        visited = set([(0,0)])
        self.dfs(robot, visited, 0, 0, direction, directions)

    def dfs(self, robot, visited, i, j, direction, directions):
        robot.clean() # 每到一个新cell就clean
        for k in range(4):
            n_direction = (direction + k) % 4 # 方向更新:当前direction顺时针转k次
            ni = i + directions[n_direction][0]
            nj = j + directions[n_direction][1]

            if (ni, nj) not in visited and robot.move():
                visited.add((ni, nj))
                self.dfs(robot, visited, ni, nj, n_direction, directions)
                self.go_back(robot) # robot参数要传
            robot.turnRight()

    def go_back(self, robot): # 两次右转等于转180度 走一步 再两次右转转180度 回到初态
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()