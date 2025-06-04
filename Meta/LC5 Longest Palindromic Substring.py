'''
回文的性质：回文字符串是中心对称的，可以从中心向两边扩展，判断是否对称。
中心选择：
回文可能是奇数长度，例如 "aba"，中心是一个字符。
也可能是偶数长度，例如 "abba"，中心是两个字符。
所以我们枚举所有中心点（共 2n - 1 个中心），从每个中心向两边扩展，找出最长回文。
更新答案：
对每个中心扩展后得到的回文子串，与当前的最长回文子串做比较，保留较长的那一个。
T(n^2) S(n) if consider tmp results p1/p2
'''
def longestPalindrome(s: str) -> str:
    if not s: return ""
    res = ""
    for i in range(len(s)):
        p1 = palindrome(s, i, i+1) # even length str
        p2 = palindrome(s, i, i)   # odd length str 
        if len(p1) > len(res):    # p1/p2都可能更新res
            res = p1
        if len(p2) > len(res):
            res = p2
    return res

def palindrome(s, left, right):
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break
    return s[left + 1: right] # 注意l+1