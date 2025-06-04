'''
字符串匹配问题
逐字符比较，如果全部匹配成功，则返回当前起始位置 否则继续下一个位置
外层循环枚举起始位置idx 最多到 (n - m):
内层循环从idx开始与needle对应位置比较字符
一旦匹配失败就提前break, 若成功走完子串返回idx
全部位置都尝试过仍未匹配到则返回 -1
T((n-m+1) * m) S(1)
'''
def str_find(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)
    for idx in range(n - m + 1): # n大 m小
        for i in range(m):
            if needle[i] != haystack[idx + i]:
                break
            if i == m - 1:
                return idx
    return -1