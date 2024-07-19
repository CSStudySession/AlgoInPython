# 用倍增的思想计算. 复杂度log(dividend)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 考虑溢出的情况: -2^31 / -1 = 2^31 --> 正溢出
        if dividend == -2**31 and divisor == -1:
            return 2**31 -1
        
        # 考虑正负号 先算出符号来
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1
        # 都转成正数算 算完再考虑符号
        dividend, divisor = abs(dividend), abs(divisor)

        # 存储指数项: exp: [2^0 * divisor, 2^1 * divisor, ..., 2^x * divisor] 
        exp = []
        cur = divisor
        while cur <= dividend:
            exp.append(cur)
            cur += cur

        # 从大到小计算商
        ret = 0
        idx = len(exp) - 1
        while idx >= 0:
            if dividend >= exp[idx]: # dividend比 2^idx * divisor 大 所以商的二级制表示中 idx位上应该是1
                dividend -= exp[idx]
                ret += 1 << idx      # 商加上2的idx次方
            idx -= 1
        return ret if sign == 1 else -ret