
# 枚举回文串可能的中心点 往两边扩散检查. 注意有两种情况:
# 1. 中心点是一个 串长为基数  2. 中心点两个 串长是偶数
# T(N^2)  S(1)
def countSubstrings(self, s: str) -> int:
    if not s:
        return 0
    ret = 0
    for i in range(len(s)):
        cnt1 = self.get_pali_number(s, i, i + 1) # 两个中心点
        cnt2 = self.get_pali_number(s, i, i)  # 一个中心点
        ret += cnt1 + cnt2 # 每个i 两种情况的结果 都更新到ret
    return ret

def get_pali_number(self, s, left, right) -> int:
    res = 0
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        else: # 需要break 某个位置开始不满足条件 后面不能再算了
            break
    return res