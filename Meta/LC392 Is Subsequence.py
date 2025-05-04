'''
思路:双指针
1. i,j分别指向s,t起点 往后遍历
  -- s[i] t[j]相等时 i,j各移动到下个位置对比
  -- 不相等时 只移动j(被匹配的动)
2. 循环结束 check i是否走到头
T(m+n) S(1)
'''
def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s)