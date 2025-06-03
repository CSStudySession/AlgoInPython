'''
variant:Assume the following rules are for the tic-tac-toe game on an 3 x 3 board between two players:
A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Write a function isWin(board, player, row, col) that takes a board state, player, and move and returns true if that player has won the game, and false otherwise.
Constraints:n == 3  player is 1 or 2. 0 <= row, col < n
Only one call will be made to isWin.
思路: 玩家在 (row, col) 落子后，可能赢的路径只有：当前行, 当前列, 主对角线（如果在对角线上）,副对角线（如果在副对角线上）
遍历一次n大小的棋盘 检查这四条路径是否都是该玩家的标记
T(n) S(1)
'''
def is_win(board, player, row, col):
    # 把当前玩家的这一步落子填入棋盘
    board[row][col] = player
    n = len(board)
    rows = 0          # 统计当前行中 player 的数量
    cols = 0          # 统计当前列中 player 的数量
    diagonal = 0      # 统计主对角线中 player 的数量
    anti_diagonal = 0 # 统计副对角线中 player 的数量
    for i in range(n):
        # 检查当前行 row 是否全是 player
        if board[row][i] == player:
            rows += 1
        # 检查当前列 col 是否全是 player
        if board[i][col] == player:
            cols += 1
        # 检查主对角线
        if board[i][i] == player:
            diagonal += 1
        # 检查副对角线
        if board[i][n - 1 - i] == player:
            anti_diagonal += 1
    # 如果任一方向达成三连，就返回 True
    return rows == n or cols == n or diagonal == n or anti_diagonal == n

'''
leetcode OG
思路:用计数法判断 每个玩家落子时 用数组记录每一行、列、对角线的得分变化
玩家1用+1代表落子 玩家2用-1代表
如果某一行或列或对角线的绝对值等于n 就说明该玩家胜出
T(1) 每步只更新常数个计数器   S(n) 两个数组
'''
class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
    def move(self, row, col, player):
        # 玩家1计为+1，玩家2计为-1
        point = 1 if player == 1 else -1
        self.rows[row] += point
        self.cols[col] += point
        if row == col:
            self.diagonal += point
        if row + col == self.n - 1:
            self.anti_diagonal += point
        # 如果任意方向累计值的绝对值等于n，表示该玩家胜出
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return player
        return 0