# 顺序遍历 用两个变量记录:
# 1. extra_close:最小增加左括号数(左括号不够了)
# 2. extra_open:最小增加右括号数(遍历结束后 有多余的左括号)
def min_add_valid(s:str) -> str:
    extra_close = 0
    extra_open = 0
    for ch in s:
        if ch == '(':
            extra_open += 1
        elif ch == ')':
            if extra_open == 0:
                extra_close += 1
            else:
                extra_open -= 1
    return extra_close + extra_open

# variant: return the string after min add.
def min_add_valid_string(s:str) -> str:
    ret = []
    extra_open = 0
    for ch in s:
        if ch == '(':
            extra_open += 1
            ret.append(ch)
        elif ch == ')':
            if extra_open == 0:
                ret.append('(')
                ret.append(ch)
                continue
            else:
                extra_open -= 1
                ret.append(ch)
        else:
            ret.append(ch)
    while extra_open:
        ret.append(')')
        extra_open -= 1
    return ''.join(ret)

# test
s = ")))" # ()()()
s = "(((" # ((()))
s = ")))(((" # ()()()((()))
s = "((a)()))((xyz" # ((a)())()((xyz))
print(min_add_valid_string(s))