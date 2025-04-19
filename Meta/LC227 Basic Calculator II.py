# 包括加减乘除 没有括号

'''
    linear scan: time O(n) space O(1)
    let ch be current char in s
    1. 如果ch.isdigit() 记录number
    2. 如果当前ch in "+-/*", 看previous sign(op): cur此时累进计算前面的+-*/
        2.1 如果当前ch in "+-", 把cur累加到ret, cur归零
        2.2 pre_op = ch(把当前ch给pre_op, 用pre_op记录previous operator), num归零
'''
def calculate0(s) -> int:
    if not s:
        return 0
    
    ret, cur = 0, 0
    pre_op = '+'

    s += '+' # 最后一个数可能会被漏掉 在s后面append一个'+' 方便计算
    num = 0 # 截取s中的数字 可能有多位数
    
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch) # 注意这里是= 不是+=
        
        if ch in ('+', '-', '*', '/'):
            if pre_op == '+':
                cur += num
            elif pre_op == '-':
                cur -= num
            elif pre_op == '*':
                cur *= num
            else: # pre_op is '/'
                cur = int(cur / num) # 有可能有负数除法 要用int() 不能用//
            # 这里的if 和下面堆pre_op/num赋值 都在ch是运算符的if条件下
            if ch in ('+', '-'):
                ret += cur
                cur = 0
            
            pre_op = ch
            num = 0

    return ret

# method 2: stack T O(n) S O(n)
def calculate1(self, s: str) -> int:
    stack = []
    num = 0
    sign = "+"
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if c in "+-*/" or i == len(s) - 1: #最后一个数 既要参与上面if计算 也要在这里计算. 所以不能用elif
            if sign == "+":
                stack.append(num)
            if sign == "-":
                stack.append(-num)
            if sign == "*":
                stack.append(stack.pop() * num)
            if sign == "/":
                stack.append(int(stack.pop() / num)) # "//"不能做负数运算 需要用int(a/b)
            
            sign = c
            num = 0
    return sum(stack)