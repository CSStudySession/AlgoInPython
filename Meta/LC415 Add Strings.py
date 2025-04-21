# variant1: both non-negative numbers may have decimals.
# e.g.: 11.1 + 123.5, 9. + 9.4, .15 + 612
# need to clarify: 1. if trailing zeros in output ok?
'''
思路: 把原题的实现当成一个helper function. 分开处理小数部分和整数部分加法.
注意 小数部分加法 要对其位数 短的小数末尾补0.
T(max_len(num1, num2)), S(max_len(num1, num2)):生成了辅助变量
'''
def addStringDecimals(num1: str, num2: str) -> str:
    if not num1 and not num2:
        return ""

    nums1 = num1.split('.') 
    nums2 = num2.split('.')
    
    has_decimal = len(nums1) > 1 or len(nums2) > 1
    decimal_s1 = nums1[1] if len(nums1) > 1 else "" # 取各自小数部分
    decimal_s2 = nums2[1] if len(nums2) > 1 else "" # 注意语法
    while len(decimal_s1) != len(decimal_s2): # 给短的小数部分补0
        if len(decimal_s1) < len(decimal_s2):
            decimal_s1 += "0"
        else:
            decimal_s2 += "0"
    ret, carry = helper_add(decimal_s1, decimal_s2, 0)
    if has_decimal: # 小数点要加在前面
        ret = "." + ret
    cur_ret, new_carry = helper_add(nums1[0], nums2[0], carry)
    ret = cur_ret + ret # 整数加法结果在前 小数加法结果在后 两部分concat
    if new_carry > 0: # 注意check最后的进位
        ret = "1" + ret
    return ret

def helper_add(num1: str, num2: str, carry: int) -> tuple[str]:
    i , j = len(num1) - 1, len(num2) - 1 # 不用特判 两个空串进来ok
    ret = ""
    while i >= 0 or j >= 0: # 注意这里是or 谁短谁当前位变0参与计算 
        a = int(num1[i]) if i >= 0 else 0
        b = int(num2[j]) if j >= 0 else 0
        sum = a + b + carry
        carry = sum // 10
        ret = str(sum % 10) + ret # 新digit放在ret最前面
        i -= 1
        j -= 1
    return (ret, carry)

# test
print(addStringDecimals("12", "9"))

# LC原题. 双指针 从后往前算. 维护carry, sum. 注意最后carray可能剩1
def addStrings(num1: str, num2: str) -> str:
    if not num1 and not num2:
        return ""
    i , j = len(num1) - 1, len(num2) - 1
    carry = 0
    ret = ""
    while i >= 0 or j >= 0: # 注意这里是or 谁短谁当前位变0参与计算 
        if i >= 0:
            a = int(num1[i])
        else:
            a = 0
        if j >= 0:
            b = int(num2[j])
        else:
            b = 0
        sum = a + b + carry
        carry = sum // 10
        ret = str(sum % 10) + ret # 新digit放在ret最前面
        i -= 1
        j -= 1
    if carry == 1:
        ret = "1" + ret
    return ret