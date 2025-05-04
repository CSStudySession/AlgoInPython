import collections
'''
双指针 
维护区间[i,j] 使得该区间内部没有重复字符 当出现重复字符时 朝j的方向移动i 
当窗口内无重复字符时 再移动j
'''
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    ret = 0
    ch_to_cnt = collections.defaultdict(int) # {char:freq}
    i, j = 0, 0
    while j < len(s):
        cur = s[j]
        ch_to_cnt[cur] += 1 # j当前字符cnt+1
        while ch_to_cnt[cur] > 1: # 刚加入的字符cnt>1 说明出现重复了
            ch_i = s[i]
            ch_to_cnt[ch_i] -= 1
            i += 1 # 移动左边的i 直到无重复字符
        ret = max(ret, j - i + 1) # 每次更新ret
        j += 1 # 移动右指针j
    return ret

# variant: 返回所有最长无重复字符的子串
'''
思路:在原solution基础上 记录满足最大长度的substring的起始index
1. 每次窗口扩张时 若 j - i + 1 == 当前最大长度，记录 s[i:j+1]
2. 若 j - i + 1 > 当前最大长度，说明找到了更长的子串 清空旧的记录 只保留新的
'''
def all_longest_substring_without_duplicates(s: str) -> int:
    if not s:
        return 0
    max_len = 0
    ret = []
    ch_to_cnt = collections.defaultdict(int) # {char:freq}
    i, j = 0, 0
    while j < len(s):
        cur = s[j]
        ch_to_cnt[cur] += 1 # j当前字符cnt+1
        while ch_to_cnt[cur] > 1: # 刚加入的字符cnt>1 说明出现重复了
            ch_i = s[i]
            ch_to_cnt[ch_i] -= 1
            i += 1 # 移动左边的i 直到无重复字符
        if j - i + 1 > max_len: # 找到更长的 清空已有结果后 加入当前子串
            ret.clear()
            ret.append(s[i: j + 1])
            max_len = j - i + 1
        elif j - i + 1 == max_len: # 与当前最长长度相等 加入结果集
            ret.append(s[i:j + 1])
        j += 1 # 移动右指针j
    return ret