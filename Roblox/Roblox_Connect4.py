'''
给定一个mxn的棋盘和一系列落子操作 2位玩家交替下棋 每一步落子后 判断当前落子的玩家是否已经连成4个:
横、竖、斜、反斜 第一个连成4个的玩家获胜 如果棋盘已满仍无人获胜 则为平局
棋盘初始为空。棋子只能从上到下落到某一列的最底部空位置
输入为操作序列 每一步由(col, player)表示落子列和玩家编号(1或2)
输出第一个获胜玩家编号 若没人获胜返回0
思路:直接模拟游戏
1. 棋盘状态
用mxn二维数组表示棋盘 如标准为6x7, 落子操作时 从底部往上找到当前列第一个空位进行填充
2. 判胜逻辑
每落一子 只需判断该点为中心的四个方向 "横、竖、两对角线" 是否存在连续4个本方棋子
3. 优化
只需判断最近落子的点 效率高 不需要全盘扫描
每次move()函数T(1) 只检查4个方向 每方向最多检查k-1个格子(k取决于题目要求 是conn4 or conn3) 
'''
class Connect4:
    def __init__(self, m=6, n=7):
        self.m = m
        self.n = n
        # self.k = 4 # 如果需要自定义连子个数
        self.board = [[0] * n for _ in range(m)]  # 0表示空
        self.next_row = [m - 1] * n  # 每列的下一个可落子的行 游戏规则默认只能从底部落子
    def move(self, col, player):
        if col < 0 or col >= self.n:
            raise ValueError("invalid colunm")
        row = self.next_row[col]
        if row < 0:
            raise ValueError("Column is full")
        self.board[row][col] = player
        self.next_row[col] -= 1
        if self.check_win(row, col, player):  # 检查胜负
            return player
        return 0  # 未分胜
    def check_win(self, row, col, player):
        # 检查4个方向
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for d in (1, -1): # 向正反两个方向分别查找
                r, c = row, col
                for _ in range(3): # 算上自己 再找3个子
                    r += dr * d
                    c += dc * d
                    if 0 <= r < self.m and 0 <= c < self.n and self.board[r][c] == player:
                        count += 1
                    else:
                        break
            if count >= 4:
                return True
        return False