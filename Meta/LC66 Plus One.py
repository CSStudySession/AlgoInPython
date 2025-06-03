'''
从数组末尾开始遍历数字：
如果当前位是 9 则加一后变为 0 继续向前进位。
如果当前位不是9 则加一后不会进位 直接返回结果即可
如果所有位都是9 最后会变成一串0 这时需要在最前面插入一个 1 表示进位

T(n) S(1)
'''
def plusOne(digits: list[int]) -> list[int]:
    if not digits:
        return []
    # 从最后一位开始遍历
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0  # 需要进位
        else:
            digits[i] += 1  # 不需要进位 直接返回
            return digits
    # 如果所有位都是9，例如999 -> 1000
    return [1] + digits