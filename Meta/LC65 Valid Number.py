
'''
note: to clarify what input str could contains: 0-9, sign, letter etc.
思路: 逐字符遍历字符串，利用状态变量来跟踪当前字符的合法性. 以下是规则:
- decimal: only once, not after exponential
- "+-" sign: only first place, or after "Ee"(不需要考虑, in case of exponential, will consider this)
- "Ee" exponential: only once, only after digit
- anything else: return False
- return digit:遍历结束后 只有当至少遇到过一个数字时 digit == True 才返回 True
'''
def is_number(s:str) -> bool:
    if not s:
        return False
    decimal, exp, digit, sign = False, False, False, False
    for ch in s:
        if ch.isdigit():
            digit = True
        elif ch in "+-":
            if digit or decimal or sign: # 见过任何这些 都违规
                return False
            else:
                sign = True
        elif ch in "Ee":
            if exp or not digit: # 见过exp 或 前面没有数字
                return False
            else:
                exp = True
                digit, sign, decimal = False, False, False # 其他三个重置
        elif ch == '.':
            if decimal or exp:
                return False
            else:
                decimal = True
        else:
            return False # 不能有任何其他字符
    return digit # 只有当至少遇到过一个数字时才是Ture 否则False

# variant: no Exponential in input
# 思路: 逐字符遍历字符串 两个状态变量 digit, decimal 来keep track of目前字符合法性
def is_valid_num(s: str) -> bool:
    if not s:
        return False
    digit, decimal = False, False
    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            digit = True
        elif ch in "+-":
            if i != 0:
                return False # 符号只可能出现在第一位
        elif ch == '.':
            if decimal:
                return False # 最多有一个小数点
            decimal = True
        else:
            return False
    return digit