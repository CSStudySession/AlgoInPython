'''
实现 Math.round() 的字符串版本
Part 1: 四舍五入到最接近的整数
输入：字符串 s 表示一个数字 可以包含小数
输出：返回四舍五入后的整数，结果仍为字符串类型。
Clarification
- 输入字符串不保证可以转换为 float 有可能过大
- 不允许直接使用 Math.round()。
- 输入保证合法（无逗号 最多一个小数点，至少一个数字，无多余前导零）
思路: 
1. 把输入分成小数和整数部分
2. 如果有小数部分 判断是否需要进位 需要的话 执行进位逻辑
'''
def round_nearest_integer(num_str: str) -> str:
    # 找小数点的位置
    if '.' not in num_str:
        return num_str  # 无小数点，直接返回
    
    dot_pos = num_str.index('.')
    integer_part = num_str[:dot_pos]
    decimal_part = num_str[dot_pos + 1:]

    # 判断是否需要进位（小数点后一位 >= 5）
    if decimal_part and int(decimal_part[0]) >= 5:
        # 需要进位，从个位开始向前加
        digits = list(integer_part)
        i = len(digits) - 1
        carry = 1
        while i >= 0 and carry:
            new_digit = int(digits[i]) + carry
            if new_digit < 10: # 发现没有进位 直接return
                digits[i] = str(new_digit)
                return ''.join(digits)
            else:
                digits[i] = '0'
                carry = 1
            i -= 1
        if carry:
            digits = ['1'] + digits
        return ''.join(digits)
    else:
        return integer_part
# test
assert(round_nearest_integer("0.5") == "1")

'''
part 2
输入：字符串 s 表示一个数（可能是整数或小数）
输出：对 s 四舍五入到更高一位，如：
153 → 200, 0.153 → 0.15, 1000.0 → 1000.0
Clarifications
- 保留原始 decimal 结构（例如 "0.15"）。
- 若已经没有可进位的位(如 "1000" 只有一位有效位) 直接返回原值。
- 可借助 Part 1 的逻辑模块。
'''
def round_to_next_place(num_str: str) -> str:
    digits = list(num_str)
    n = len(digits)

    # Step 1: 从右往左找到第一个非 0 的 digit（即 round_base_index）
    round_base_index = -1
    for i in range(n - 1, -1, -1):
        if digits[i].isdigit() and digits[i] != '0':
            round_base_index = i
            break
    if round_base_index <= 0:
        return num_str  # 只有1位有效数字 没法round了

    # Step 2: 判断 round_base 自身是否 ≥ 5
    if digits[round_base_index] >= '5':
        # 向左一个 digit 进位（如果有）
        j = round_base_index - 1
        carry = 1
        while j >= 0 and carry:
            if not digits[j].isdigit():
                j -= 1
                continue
            val = int(digits[j]) + carry
            if val < 10:
                digits[j] = str(val)
                carry = 0
            else:
                digits[j] = '0'
                carry = 1
            j -= 1
        if carry:
            digits = ['1'] + digits
            round_base_index += 1  # 位置右移了
    
    digits[round_base_index] = '0' # 不管怎样 这一位都得变'0'
    # Step 4: 返回结果（可选去掉尾部 0）
    result = ''.join(digits)
    if '.' in result: # 当有小数点时 先去除尾部多余的0 再去除尾部的小数点
                      # 如果最后只剩下空串'' 返回一个'0'
        result = result.rstrip('0').rstrip('.') or '0'
    return result

# test
# print(round_to_next_place('2.926189'))

'''
part 3
给定两个字符串: s为要round的数字(如 "0.256") p表示需要round到哪一位的单位(如 "0.1", "100", "0.01")
输出round的结果
思路: 
1. 计算 s/p -> "0.256" / "0.1" = "2.56"
2. 转化成part2的问题 调用part2的code直接算 记结果为r -> 2.6
3. result = r * p -> 2.6 * 0.1 = 0.26
'''
from decimal import Decimal

def round_to_place(s: str, p: str) -> str:
    s_val = Decimal(s)
    p_val = Decimal(p)
    # Step 1: 除法：缩放成整数范围
    scaled = s_val / p_val  # 例如 0.256 / 0.1 = 2.56
    # Step 2: 调用已有的字符串in part2
    rounded_scaled_str = round_to_next_place(str(scaled))  # 如 "2.56" → "2.6"
    rounded_scaled = Decimal(rounded_scaled_str)
    # Step 3: 乘回原位
    result = rounded_scaled * p_val  # 3 * 0.1 = 0.3
    # Step 4: 去除尾部无效 0（如有需要）
    result_str = format(result, 'f')  # 不使用科学计数法
    if '.' in result_str:
        result_str = result_str.rstrip('0').rstrip('.') or '0'
    return result_str

print(round_to_place('1.99', '1'))

'''
part 4. 输入s: 字符串数字 n:要保留的有效数字个数(significant digits) 输出string表示
思路:
1. 找到第sig_digits+1位的数 它决定是否要进位
  -- 如果有效数字不够sig_digits个 补0
2. 判断是否需要进位 需要的话 进行按digit加法的操作
3. 记sig_digits-1位为keep_idx 从keep_idx+1开始 都set digit to '0'
'''
def round_to_sig_digits(num_str: str, sig_digits: int) -> str:
    if len(num_str) <= 1:
        return num_str
    digits = list(num_str)
    # Step 1: 收集所有 digit 的位置
    digit_indices = [i for i, ch in enumerate(digits) if ch.isdigit()]
    # 有效数字不足时补0
    if len(digit_indices) < sig_digits:
        digits_needed = sig_digits - len(digit_indices)
        if '.' not in num_str:
            digits.append('.')
        while digits_needed:
            digits.append('0')
            digit_indices.append(len(digits) - 1)
            digits_needed -= 1
    # 补0之后的有效位数 刚好等于sig_digits->不需要round 直接返回
    if len(digit_indices) == sig_digits:
        return ''.join(digits)

    # 找第 sig_digits 位（要保留的最后一位），以及下一位（决定是否进位）
    keep_index = digit_indices[sig_digits - 1]
    round_index = digit_indices[sig_digits]  # 第sig_digits+1 位，决定进位与否

    # Step 2: 判断是否需要进位
    if digits[round_index] >= '5':
        # 向 keep_index 进位（有 carry）
        j = keep_index
        carry = 1
        while j >= 0 and carry:
            if not digits[j].isdigit():
                j -= 1
                continue
            val = int(digits[j]) + carry
            if val < 10:
                digits[j] = str(val)
                carry = 0
                break
            else:
                digits[j] = '0'
                carry = 1
            j -= 1
        if carry:
            digits = ['1'] + digits
            keep_index += 1  # 因为整体右移了

    # Step 3: 清除 keep_index 右边所有 digit（只清 digit，不动小数点）
    cleared = 0
    for i in range(keep_index + 1, len(digits)):
        if digits[i].isdigit():
            digits[i] = '0'
            cleared += 1

    # Step 4: 构造返回结果
    result = ''.join(digits)
    return result

# test
print(round_to_sig_digits('1555', 1))
print(round_to_sig_digits('1.56', 2))