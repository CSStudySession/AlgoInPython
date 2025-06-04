'''
思路:
去除前导空格：用 strip() 去除首尾空格；
判断符号位：若首字符是 '+' 或 '-'，记录符号；
遍历字符并构造整数：从当前位置开始，遍历数字字符构造整数；
处理非法字符：遇到非数字字符就停止转换；
溢出处理：结果若超过 32 位整数范围，则按上/下界截断返回。
T(n) S(1)
'''
def myAtoi(s: str) -> int:
    # 去除前后空格
    s = s.strip()
    if not s:
        return 0  # 空字符串直接返回0
    sign = 1  # 默认为正数
    res = 0
    maxInt = 2**31 - 1  # 32位整数上限
    minInt = -2**31     # 32位整数下限
    start = 0 # 从0开始检查
    # 判断符号位
    if s[0] == "-":
        sign = -1
        start += 1
    elif s[0] == "+":
        start += 1
    # 遍历后续字符
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break  # 遇到非数字字符 停止转换 后面不用看了
        # 构造数字 自动处理前导0
        res = res * 10 + int(s[i])
    # 加上符号
    res *= sign
    # handle overflow 
    if res < minInt:
        return minInt
    if res > maxInt:
        return maxInt
    return res

