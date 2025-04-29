
# 注意这题要求返回所有结果 不是只返回任意一个. 要用DFS解决.
'''
1. 先计算多余的 ( 和 ) 数量。
2. 用DFS删除多余括号 递归遍历所有删除括号的合法位置
3. 在同一递归层中跳过重复字符 去重:if i > start and s[i] == s[i - 1]
字符串: "()())"
           ^^ 两个连续的 ')'
删除第一个 ) → "()()",删除第二个 ) → "()()" 结果相同 所以只在第一个')'dfs即可
4. check左右多余括号数量最终都为0
T(2^n) S(n) n是括号数量 每个括号都可以删或者不删
'''
def removeInvalidParentheses(s: str) -> list[str]:
    ret = []
    left, right = get_invalid_count(s)
    dfs(left, right, 0, s, ret)
    return ret

def dfs(left, right, start, remaining, ret):
    if left == 0 and right == 0:
        l, r = get_invalid_count(remaining) # 最后check一下是否有多余的括号
        if l == 0 and r == 0:
            ret.append(remaining)
        return
    
    for i in range(start, len(remaining)):
        if i > start and remaining[i] == remaining[i - 1]:
            continue
        if left > 0 and remaining[i] == '(': # 注意if..elif的关系 s[i]是'('或')' 是互斥的 
            dfs(left - 1, right, i, remaining[:i] + remaining[i+1:], ret)
        elif right > 0 and remaining[i] == ')':
            dfs(left, right - 1, i, remaining[:i] + remaining[i+1:], ret) 

def get_invalid_count(s):
    left, right = 0, 0
    idx = 0
    while idx < len(s):
        if s[idx] == '(':
            left += 1
        elif s[idx] == ')':
            if left == 0:
                right += 1
            else:
                left -= 1
        idx += 1
    return left, right