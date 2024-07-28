'''
双指针 
维护区间[i,j] 使得该区间内部没有重复字符 当出现重复字符时 朝j的方向移动i 当窗口内无重复字符时 再移动j
'''
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        n, ret = len(s), 0
        map = defaultdict(int) # str:freq

        # 双指针模板
        i, j = 0, 0
        while j < len(s): 
            map[s[j]] += 1 # j对应的字符freq+1 
            while map[s[j]] > 1: # 出现重复字符了:刚加入的字符freq大于1
                map[s[i]] -= 1   # i指向的字符滑出窗口 freq-1
                i += 1           # 移动i
            ret = max(ret, j - i + 1) # 每一步更新见过的窗口大小
            j += 1 # 用while要记得显示写j+=1 
        return ret