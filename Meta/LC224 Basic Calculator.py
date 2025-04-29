
'''
# 有加减和括号
数字：更新 num 注意多位数字要累加 例如"12"要处理成 1*10+2=12。
加号 +：把之前解析的数字按照之前的符号累加到 res 然后把 sign 置为 +1 准备处理下一个数字
减号 -：同理，先累加当前数字到 res 然后把 sign 置为 -1。
左括号 (：表示进入一个新的子表达式。此时需要：
- 把当前的 res 和 sign 保存到 stack。
- 将 res 和 sign 重置为 0 和 1 以便单独计算括号内的表达式。
右括号 )：表示括号内的子表达式结束。此时需要：
- 先将当前 num 应用符号累加到 res。
- 弹出之前保存的 sign 用来乘上当前括号内的结果。
- 弹出之前保存的 res 加到乘好符号后的括号结果上。
T(n) S(n)
'''
def calculate(s: str) -> int:
    num = 0
    res = 0
    sign = 1
    stack = []
    for ch in s:
        if ch.isdigit():
            num = 10 * num + int(ch)
        elif ch == "+":
            res += sign * num
            num = 0
            sign = 1 # 把现在的sign交给下一次
        elif ch == "-":
            res += sign * num
            num = 0
            sign = -1 # 更新sign
        elif ch == "(":
            stack.append(res) # 需要append previous res(不是num)&sign, then reset
            stack.append(sign)
            sign = 1 # 交出去给stack之后需要重置
            res = 0
        elif ch == ")":
            res += sign * num # 结算当前括号里的结果(同+-时候的情况)
            res *= stack.pop() #pop previous sign
            res += stack.pop() #pop previous res
            num = 0
            sign = 1
    if num != 0: # 最后还有一位没有结算
        res += sign * num
    return res
