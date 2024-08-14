'''
https://leetcode.com/problems/shortest-way-to-form-string/description/
A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source 
such that their concatenation equals target. If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

Constraints:
1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.

思路: 
1.用一个二维哈希表(或者二维数组)index_to_next来表示当前source的index右边(包括index本身)每一个字母第一次出现的位置的下一个位置。
比如abbc 那么index[0]['a']=1 index[0]['b'] = 2, index[1]['b']= 2, index[2]['b']= 3..从右向左遍历一遍source即可完成更新index_to_next
2.然后遍历target, source和target的位置分别记为i和j 我们执行以下操作:
1.index_to_next[0]当中是否存在target[j] 即整个source中是否存在j 不存在则返回-1
2.index_to_next[i]当中是否存在target[j] 如果不存在 说明source在位置i右侧不存在target[j] i应当归零从头开始找
3.如果i == 0 说明source被遍历了一边 返回值round++ 
4.更新i = index_to_next[i][target[j]] 即source中i右侧第1个target[j]的右侧的位置 
这样相当于在source中读取了一个最近的target[j]
5.最后返回round即可。

time O(m+n) space O(m)(dict的第二维 key最多26个字符), m:len(src) n:len(trgt) 
''' 
from collections import defaultdict

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not source or not target:
            return -1
        
        # dict[int1, dict[str, int2]]
        # int1:src当前的index, int2:src读取完str后 对应的下一个index
        index_to_next = defaultdict(dict)
        index_to_next[len(source) - 1][source[-1]] = 0 # src在最后一个位置 读取完自己后 应该回到起点重新寻找匹配
        for i in range(len(source) - 2, -1, -1):
            index_to_next[i] = index_to_next[i + 1].copy() # 注意这里要copy 不能直接赋值
            index_to_next[i][source[i]] = i + 1
        
        round, i = 0, 0
        idx = 0
        while idx < len(target):
            # 整个src中没有trgt[idx]这个字符
            if target[idx] not in index_to_next[0]:
                return -1
            # src的当前位置i后面找不到trgt[idx]的字符 应当返回src的起始位置重新找
            if target[idx] not in index_to_next[i]:
                i = 0
            if i == 0: # 每次i归零 证明匹配过一次了
                round += 1
            # i更新为 离i最近的trgt[idx]的右边一位
            i = index_to_next[i][target[idx]]
            idx += 1
        return round