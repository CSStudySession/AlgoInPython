from collections import defaultdict
'''双指针
- left right 指向滑动窗口的两端
用dict来记录每个字符 在窗口中的最右端出现位置
- 主循环 遍历字符串用右指针right
每次将字符 s[right] 加入 hashmap 记录其位置
  - 如果dict中有 超过两个不同字符 即大小为3
找到当前窗口中最左侧字符 即位置最小的字符 将其从hashmap中删除
  - 将left指针移动到这个字符后面
  - 每次更新窗口长度 right - left + 1维护最大值
  - right += 1
T(n) S(1)
'''
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    n = len(s)
    if n < 3:
        return n
    left, right = 0, 0
    hashmap = defaultdict() # char -> rightmost pos in window
    max_len = 2
    while right < n:
        hashmap[s[right]] = right
        # slidewindow contains 3 characters
        if len(hashmap) == 3:
            del_idx = min(hashmap.values())  # delete the leftmost char
            del hashmap[s[del_idx]]
            left = del_idx + 1  # move left ptr to del_idx + 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len