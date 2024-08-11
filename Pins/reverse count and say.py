'''
leetcode link: https://leetcode.com/discuss/interview-question/algorithms/124839/pinterest-reverse-count-and-say

Given an input string which is the output of a "count and say method", return the original number.
For example: If the number if "21", then the count and say method would return "1211" (one two, one one). 
In this problem, the input provided to us is "1211" and our goal is to return "21".

'''
from typing import List
from collections import defaultdict

def reverseCountSay(s:str) -> set[str]:
    if not s:
        return {}
    # str: List[List[str]]
    # 
    memo = defaultdict(list)  
    recursive(s, memo)

    ret = set()              # return a set to make values unique
    for output in memo[s]:   
        joined_output = ''.join(output)  # output可能是['2', '1'] join完之后是'21'
        ret.add(joined_output)
    return ret        

'''
递归过程：
递归过程中，首先处理 s 的前 i 位作为重复次数 cnt, 然后将第 i 位之后的字符作为重复的字符 cur_num, 继续递归处理剩余的字符串。
对于每个递归返回的子结果sub_ret, 将当前字符重复 cnt 次后与子结果连接起来，形成一个完整的组合。
'''
def recursive(s:str, memo:dict[str, List[List[str]]]) -> List[List[str]]:
    if len(s) == 0:
        return [[]]
    
    elif s in memo:
        return memo[s]
    
    # 有个corner case 该程序可以handle. 当s被某种不合法的方式切成只有一个字符时 比如此时s：”1“
    # 它会跳过下面的循环 因为它没有下标为1的index 然后直接执行return memo[s]
    # defaultdict会直接返回一个空list 不会出异常:非法的字符解码成空list 
    for i in range(1, len(s)):                        # 从下标1开始 起码要留出1位给个数cnt
        cur_num, cnt = s[i], int(s[:i])               # s的前i位作为重复次数cnt,将第i位的字符作为重复的字符cur_num
        for sub_ret in recursive(s[i + 1:], memo):    # 继续递归处理剩余的字符串
            memo[s].append([cur_num * cnt] + sub_ret) # 将当前字符重复cnt次后与子结果sub_ret连接起来 形成一个完整组合

    return memo[s]


s1 = "1211"     # 21, 11111...(121个1)
s2 = "21"       # 11
s3 = "11"       # 1
s4 = "13112221" # 312211
s5 = ""
print(reverseCountSay(s1))
# print(reverseCountSay(s4))
print(reverseCountSay(s5))

'''
输入 "1211" 的处理过程
对于输入 "1211"，递归的处理过程如下：
第一次递归：
i = 1 时, cnt = 1, cur_num = 2, 剩余字符串为 "11"。
递归处理 "11"。
处理 "11" 的递归：
i = 1 时, cnt = 1, cur_num = 1, 剩余字符串为空。
递归处理空字符串返回 [[]]，此时组合为 ['1']。
回溯：
递归返回后，组合为 ['2'] + ['1'] = ['21']。

继续递归：
在原始递归中, i = 2 时, cnt = 12, cur_num = 1, 剩余字符串为 "1"。
递归处理 "1" 返回 [[]]。"1"单独无法解码 因为它无法被拆解成”x个y“这样的方式
或者是121次1后加1。因此 "111..."（即 121 个 1)是一个合法解。
'''