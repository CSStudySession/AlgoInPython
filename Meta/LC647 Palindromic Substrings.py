
# 枚举回文串可能的中心点 往两边扩散检查. 注意有两种情况:
# 1. 中心点是一个 串长为基数  2. 中心点两个 串长是偶数
# T(N^2)  S(1)
def countSubstrings(s: str) -> int:
    if not s:
        return 0
    ret = 0
    for i in range(len(s)):
        cnt1 = get_pali_number(s, i, i + 1) # 两个中心点
        cnt2 = get_pali_number(s, i, i)  # 一个中心点
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

'''
variant: check if given str contains a substring that is a palindrome of length equal to or greater than k.
思路: 枚举回文串可能的中心点 往两边扩散检查. 回文为奇数或偶数长度分别检查 如果有一个是True 返回True. 都遍历完了返回False
注意helper函数如何统计回文长度
T(n^2) S(1)
'''
def check_palindrome_length_k(s: str, k:int) -> bool:
    if not s or len(s) < k:
        return False
    for i in range(len(s)):
        has_palin_two = check_palin_length(s, i, i + 1, k) # 两个中心点
        has_palin_one = check_palin_length(s, i, i, k)  # 一个中心点
        if has_palin_two or has_palin_one:
            return True
    return False

def check_palin_length(s, i, j, k) -> bool:
    cnt = 0
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            if i == j:
                cnt += 1
            else:
                cnt += 2
            i -= 1
            j += 1
            if cnt == k:
                return True
        else:
            break
    return False

# test
s = "abccba"
k = 6 # True
s = "abcde"
k = 3 # False
print(check_palindrome_length_k(s, k))