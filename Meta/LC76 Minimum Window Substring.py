
import collections
'''
双指针维护一个window 两个counter:seen and need
need记录目标字符串t中每个字符的需求量,seen记录当前窗口中每个字符的实际数量
右边界扩展 逐步扩展窗口 直到包含所有目标字符
左边界收缩 在满足条件的前提下 尽量缩小窗口 找到最小的符合条件的窗口
更新答案 在每次满足条件时 检查并更新最小窗口
终止条件: 右指针遍历完整个字符串s后 返回最终结果
T(m+n) S(m+n)
'''
def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    seen, need = collections.Counter(), collections.Counter(t)
    left, right, cnt = 0, 0, 0
    min_len = float('inf')
    start = 0

    while right < len(s):
        ch = s[right]
        if ch in need: # 注意ch在need中 seen对应要+1
            seen[ch] += 1
            if seen[ch] <= need[ch]: # 先更新seen再更新cnt
                cnt += 1
        
        while cnt == len(t): # 满足条件时 先更新答案 再移动左窗口
            # 更新min_len
            if right - left + 1 < min_len:
                start = left
                min_len = right - left + 1
            # 移动左窗口
            ch_left = s[left]
            if ch_left in need: # 只要在need中 seen对应-1 与上面+1保持对应
                seen[ch_left] -= 1
                if seen[ch_left] < need[ch_left]: # 先更新seen 所以严格小于need cnt才-1
                    cnt -= 1
            left += 1 # 更新左右指针
        right += 1
    return "" if min_len == float('inf') else s[start: start + min_len]