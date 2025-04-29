# 用stack顺序记录左括号 如果当前是右括号 直接看栈顶是否匹配
# 注意这题与其他括号匹配的区别 由于有多种括号 这里类似'([)]'是不合法的  
def isValid(s: str) -> bool:
    if not s: return True
    mapping = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if ch not in mapping: # 不是右括号 一定是左括号 
            stack.append(ch) # 左括号压栈
        elif stack and stack[-1] == mapping[ch]:
            stack.pop() # 当前右括号与stack top match
        else:
            return False
    return len(stack) == 0 # 注意检查stack是否为空