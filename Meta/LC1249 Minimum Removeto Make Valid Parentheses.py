'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''

'''
solution 1: two pass
只有左右括号匹配 才算balanced
first pass to count number of '('
second pass:
遍历过程中 记录左括号个数left. 当前字符char 分类讨论:
1. char == ')'. 
  - if left>0 -> 左边有对应的匹配. char加入ret, left--.
  - else 左边没有‘（’与之匹配. right-- 避免右边的'('跟自己匹配.
2. char == '('.
  - 

'''

def minRemoveToMakeValid0(s: str) -> str:
    if not s:
        return ""
    
    right = 0
    for char in s:
        if char == ')':
            right += 1
    
    ret = []
    left = 0
    for char in s:
        if char == ')':
            if left > 0:
                ret.append(char)
                left -= 1 # 与当前')'配对
            else:
                right -= 1 # 防止与后面的'('配对
        elif char == '(':
            if right > 0:
                ret.append(char)
                left += 1 # 必须+=1
                right -= 1 # 与当前的配对
        else:
            ret.append(char)
    return "".join(ret)


    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_pass_chars.append(c)

    # Pass 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    for c in first_pass_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue
        result.append(c)

    return "".join(result)


def minRemoveToMakeValid1(self, s: str) -> str:
    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_pass_chars.append(c)

    # Pass 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    for c in first_pass_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue
        result.append(c)

    return "".join(result)