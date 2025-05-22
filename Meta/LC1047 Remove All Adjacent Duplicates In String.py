# variant: return final string after all dup removed.
# e.g. s:'abbbacxdd' -> s:'cx'   s:'azxxxzy' -> s:'ay'

# 思路:stack 栈上存[元素，出现次数] 遍历s 更新stack
# 在栈pop之后 重新判断是否需要合并当前字符
def remove_all_duplicates(s:str) -> str:
    if not s:
        return  ""
    stack = []
    for ch in s:
        if not stack:
            stack.append([ch, 1])
            continue # continue掉 避免后面逻辑混乱
        if stack[-1][0] == ch: # 注意这里ch是变量 不是'ch'
            stack[-1][1] += 1
            continue

        if stack[-1][1] > 1:
            stack.pop()
        if not stack or stack[-1][0] != ch:
            stack.append([ch, 1])
        elif stack[-1][0] == ch:
            stack[-1][1] += 1

    if stack and stack[-1][1] > 1: # 最后一个元素在stack上做处理
        stack.pop()
    ret = []
    for item in stack:
        ret.append(item[1] * item[0])
    return ''.join(ret)

# followup:如何解决这种用例"aabbccba" → ""？用上面发的方法 返回"ba" 不是""
def solve_substring(s: str, memo: dict) -> str:
    """
    递归:对字符串s枚举任意一对相邻相同字符的删除
    递归求得删除后的最短剩余串 然后在所有候选中取最优 
    使用memo记录已经计算过的s->最优结果 避免重复
    """
    if s in memo:
        return memo[s]
    
    n = len(s)
    best = s  # 初始化：不删任何字符，剩余就是 s 本身
    i = 0
    # 遍历所有可能的删除点
    while i < n - 1:
        if s[i] == s[i+1]:
            # 删除 s[i:i+2]
            t = s[:i] + s[i+2:]
            # 递归求子问题的最短剩余串
            rem = solve_substring(t, memo)
            # 更新最优：优先最短长度，其次字典序
            if len(rem) < len(best) or (len(rem) == len(best) and rem < best):
                best = rem
            # 跳过相同字符段，避免多次对同一批连续字符重复删除
            j = i + 2
            while j < n and s[j] == s[i]:
                j += 1
            i = j
        else:
            i += 1
    
    memo[s] = best
    return best
def remove_all_duplicates_memo(s: str) -> str:
    memo = {}
    return solve_substring(s, memo)
s = "aabbccba"
#s = "abccbccba"
print(remove_all_duplicates_memo(s))

# test
s = "abbaxx"  # ""
# s = "abcdefg" # "abcdefg"
# s = "aabccddeeffbbbbbbbbbf" # "f"
# s = "abbbacca" # "a"
# print(remove_all_duplicates(s))

# variant: removal rule is 3 or more duplicates left-to-right.
def remove_duplicates_by_three(s:str) -> str:
    if not s:
        return  ""
    stack = []
    for ch in s:
        if not stack:
            stack.append([ch, 1])
            continue # continue掉 避免后面逻辑混乱
        if stack[-1][0] == ch: # 注意这里ch是变量 不是'ch'
            stack[-1][1] += 1
            continue

        if stack[-1][1] >= 3:
            if stack[-1][1] % 3 == 0:
                stack.pop()
            else:
                stack[-1][1] = stack[-1][1] % 3
        if not stack or stack[-1][0] != ch:
            stack.append([ch, 1])
        elif stack[-1][0] == ch:
            stack[-1][1] += 1

    if stack and stack[-1][1] >= 3: # 最后一个元素在stack上做处理
        if stack[-1][1] % 3 == 0:
            stack.pop()
        else:
            stack[-1][1] = stack[-1][1] % 3
    ret = []
    for item in stack:
        ret.append(item[1] * item[0])
    return ''.join(ret)

s = "aaabbbacd" # "acd"
s = "aabbbacd"  # "cd"
s = "aaabbbc" # c
s = "aaaabbbacd" # "aacd" 
s = "abbcccbd" # "ad"
# print(remove_duplicates_by_three(s))

# OG below
# 解法1: stack 注意当栈顶元素与当前元素相等时 只pop一次 满足一次只能移除两个的条件
def removeDuplicates(s: str) -> str:
    if not s:
        return ""
    stack = []
    for ch in s:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
    return ''.join(stack)