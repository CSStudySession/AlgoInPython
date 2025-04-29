
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
print(remove_duplicates_by_three(s))




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