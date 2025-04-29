from typing import List
import collections
# 把rotate后 根一样的字符串group到一起 用dict维护 {root: list of strings with same root}
# group方法:把所有string都转化成以a开头的string. 
# e.g. xyz->abc 先计算第一个字母和a的差值 后面apply相同diff. 注意 ch-diff < "a"的情况 需要ch+26
# python字母ord("a") = 97 取数字ord(ch) 取字母chr(num)
# T(num of chars in strings) S(num of chars in strings)
def groupStrings(strings: List[str]) -> List[List[str]]:
    root_to_strs = collections.defaultdict(list)
    for string in strings:
        key = get_rotation_root(string)
        root_to_strs[key].append(string)
    return list(root_to_strs.values())

def get_rotation_root(string:str) -> str:
    if not string:
        return string
    diff = ord(string[0]) - ord('a') # 首字母变成'a'时 与'a' 相差几步
    curr = []
    for i in range(len(string)): # 所有字符都apply相同diff
        new_ch = chr( (ord(string[i]) - diff + 26) % 26 )
        curr.append(new_ch)
    return ''.join(curr)

#variant: given a rotate_factor. perform rotate. input could include:
# 1. lower or upper letters, digits. perform rotate
# 2. other chars, remain unchanged.
'''
与原题相比 不需要每个字符串计算原始rotate ref了. 直接在input上进行向右rotate即可.
对 digit, upper/lower letters 分类讨论. 其他字符不变.
T(len(string)) S(len(string))->辅助list ret
'''
def rotate_by_factor(string:str, factor:int) -> str:
    if not string:
        return string
    ret = [] # 用''.join()操作更efficient
    for ch in string:
        if 'a' <= ch <= 'z': # 字符可以直接比大小
            new_ch = chr( (ord(ch) - ord('a') + factor) % 26 + ord('a') )
            ret.append(new_ch)
        elif 'A' <= ch <= 'Z':
            new_ch = chr( (ord(ch) - ord('A') + factor) % 26 + ord('A') )
            ret.append(new_ch)
        elif '0' <= ch <= '9':
            new_ch =  chr( (ord(ch) - ord('0') + factor) % 10 + ord('0') )
            ret.append(new_ch)
        else:
            ret.append(ch)
    return "".join(ret)

# test
string = "89-yfZZ@" # "12-biCC@"
print(rotate_by_factor(string, 3)) 