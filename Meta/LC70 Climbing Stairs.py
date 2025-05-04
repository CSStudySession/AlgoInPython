'''
爬到第n阶的方法数=爬到第n-1阶的方法数+爬到第n-2阶的方法数
  -- 要么从 n-1 阶走 1 步上来，要么从 n-2 阶走 2 步上来。
使用Memoization:加一个memo数组来存储已经计算过的结果
T(n) S(n)
'''
def climbStairs(n: int) -> int:
    memo = [0] * (n + 1)
    return memo_search(n, n, memo)

def memo_search(i: int, n: int, memo: list[int]) -> int:
    if i == 0 or i == 1:
        return 1
    if memo[i] > 0:
        return memo[i]
    memo[i] = memo_search(i - 1, n, memo) + memo_search(i - 2, n, memo)
    return memo[i]