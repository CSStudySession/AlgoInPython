from typing import List
import collections

class Solution:
    # ref: group anagram. 把根一样的group到一起 hashmap: key-> [list]
    # 如何group: 把所有string都转化成以a开头的string. eg, xyz->abc 先计算第一个字母和a的差值 后面diff相同. 特殊注意‘b'-diff < "a"的情况 需要把"b"+26
    # #python字母ord("a") = 97 取数字ord(string), 取字母chr(num) 
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for string in strings:
            key = self.getShiftedString(string)
            dict[key].append(string)
        return list(dict.values())
    
    def getShiftedString(self, s):
        diff = ord(s[0]) - ord("a") # python字母ord("a") = 97
        shifted = ""
        for i in range(0, len(s)):
            # 考虑s[i]-diff<0的情况 需要套圈+26(). 因为python字母从97开始, 所以取mod, 这样所有情况都+26即可     
            shifted += chr((ord(s[i]) + 26 - diff) % 26)
        return shifted