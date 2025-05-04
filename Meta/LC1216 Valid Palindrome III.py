
'''
思路:memo 找出"最少需要删除多少字符"才能让这个字符串变成回文 如果这个最小删除次数 ≤ k 即满足条件
- 定义递归函数 dfs(i, j) 表示将字符串 s[i...j] 变成回文所需的最小删除次数
  - 如果 s[i] == s[j] 递归 dfs(i+1, j-1) 中间的部分决定最终结果
  - 如果 s[i] != s[j] 那就只能删除一个字符 
    - 要么s[i]->dfs(i+1, j),要么s[j] 即dfs(i, j-1) 取较小值+1
- 使用dict memo记录中间结果 避免重复计算
T(n^2):i,j组合最多n^2  S(n^2):memo大小. dfs stack at most O(n) 
'''
def isValidPalindrome(s: str, k: int) -> bool:
    memo = {}
    cnt = dfs(0, len(s) - 1, s, memo)
    return cnt <= k
def dfs(i, j, s, memo) -> int:
    if i == j:
        return 0 # 指针相遇 不需要删任何字符
    if i == j - 1:
        return 1 if s[i] != s[j] else 0
    if (i, j) in memo:
        return memo[(i,j)]
    cnt = 0
    if s[i] == s[j]: # 不需要跳过 i,j指针各走一步
        cnt = dfs(i + 1, j - 1, s, memo)
    else: # 跳过i和跳过j 取小的 然后+1(用掉了一次跳过)
        cnt = 1 + min(dfs(i + 1, j, s, memo), dfs(i, j - 1, s, memo))
    memo[(i, j)] = cnt
    return cnt