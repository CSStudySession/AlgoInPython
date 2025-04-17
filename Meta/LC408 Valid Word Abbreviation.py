'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
'''

'''
solution: two pointers T: O(n)  S: O(n)for tmp字符串构建  
'''

def validWordAbbreviation(word: str, abbr: str) -> bool:
    if len(word) < len(abbr): return False # word比abbr还短 一定不会匹配 

    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if word[i] != abbr[j]:
            if abbr[j] == '0' or not abbr[j].isdigit():
                return False
                
            tmp = '' # 截取abbr当前的数字段
            while j < len(abbr) and abbr[j].isdigit():
                tmp += abbr[j]
                j += 1
            i += int(tmp) # i跳过长度为tmp的字符串
        else: # 两个字符相等 各进一步
            i += 1
            j += 1
    return i == len(word) and j == len(abbr) # 一定要都恰好走到最后一个