'''
https://leetcode.com/problems/longest-common-prefix/description/?envType=company&envId=apple&favoriteSlug=apple-three-months

竖着一个个字符对比即可 

followup: 如果多次query LCP 怎么处理? --> 用trie. 用strs里的字符串建立trie 然后来一个query就用trie做前缀匹配
'''
from typing import List

class Solution:
    # time O(S), where S is the total lenth of all str in strs. space: O(1) 
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])): # 最长前缀不会超过strs[0]的长度
            char = strs[0][i] # 取出第i个字符
            for j in range(1, len(strs)): # 遍历剩下字符串j的每一个字符
                if i == len(strs[j]) or strs[j][i] != char: # 第j个字符走到头 或者 第i个字符与strs[j][i]不匹配
                    return strs[0][:i] # [:i]左闭右开
        return strs[0]