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
例子 s: 1+(2-3) 
ch = 1: 构建数字1 
ch = +: 处理前一个数: res+=sign*num=1 reset num=0, sign=1
ch = (: res/sign push stack: [1(res), 1(sign)] reset res=0 and sign=1
ch = 2: 构建数字2
ch = -: 处理前一个数: res += sign*num=0+1*2=2 reset num=0, sign=-1(本次为-号)
ch = 3: 构建数字3
ch = ): 处理前一个数: res += sign*num=2+(-1)*3=-1, pop stack:sign=1, pop stack:res=1
merge res=1+1*(-1)=0
'''
def calculate(s: str) -> int:
    num = 0
    res = 0
    sign = 1
    stack = []
    s += '+' # 补充+ 让最后一个运算数可以加入到结果
    for ch in s:
        if ch.isdigit():
            num = 10 * num + int(ch) # 这里是= 不是+=
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
    return res