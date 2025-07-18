from typing import List, collections
'''
思路:
第一遍遍历（从左往右）去除所有多余的右括号 )
用etr_open记录当前未匹配的左括号数量 每当遇到 ) 时
- 如果没有可匹配的左括号 跳过这个 )
- 否则减少一个未匹配的左括号etr_open-=1 并保留 )
第二遍遍历（从左往右）
去除多余的左括号 (
因为第一遍没有去处理过多的 (，我们需要移除最右边多余的那几个
最终构造结果字符串 只包含有效的括号和所有字母

'''
def minRemoveToMakeValid0(s: str) -> str:
    # Pass 1: Remove all invalid ")"
    first_pass_chars = []
    tot_open = 0   # 总共的左括号
    etr_open = 0   # 未match到右括号的左括号
    for c in s:
        if c == "(":
            tot_open += 1
            etr_open += 1
        if c == ")":
            if etr_open == 0:
                continue
            etr_open -= 1
        first_pass_chars.append(c) # 除了')'没有匹配的情况 其他都append

    # Pass 2: Remove the rightmost "("
    result = []
    net_open = tot_open - etr_open
    for c in first_pass_chars:
        if c == "(":
            if net_open == 0:
                continue
            net_open -= 1
        result.append(c)
    return "".join(result)

s1 = "(((("
s2 = "((a))"
s3 = "((a))))))"
print(minRemoveToMakeValid0(s3))

# meta variant1 : 输入是list且must do update in-place
def minRemoveToMakeValid1(s: List[str]) -> List[str]:
    if not s:
        return []
    end = 0
    tot_open, etr_open = 0, 0
    for i in range(len(s)):
        if s[i] == ')':
            if etr_open == 0:
                continue
            etr_open -= 1
            s[end] = s[i]
            end += 1
        elif s[i] == '(':
            tot_open += 1
            etr_open += 1
            s[end] = s[i]
            end += 1
        else:
            s[end] = s[i]
            end += 1
    
    net_open = tot_open - etr_open
    j = 0
    for i in range(end):
        if s[i] == '(':
            if net_open == 0:
                continue
            net_open -= 1
            s[j] = s[i]
            j += 1
        else:
            s[j] = s[i]
            j += 1
    return s[:j]    

# test
s1 = ['(', ')', '(', '(', 'a', ')']
s2 = ['(', ')', '(', '(', 'a']
s3 = ['(', ')', '(', '(', 'a', 'b', ')', ')', ')']
print(minRemoveToMakeValid1(s3))

# variant2: what if different type of parenttheses were given:(),{},[]?
# 思路:用dict表示每种括号的匹配 以及用dict表示每种括号的匹配个数
# tip: 面试时 主动问input的长度范围 可能直接规避掉edge cases:empty, null etc.
# T(n) S(n) 辅助dict的长度是固定的 返回值不算 tmp str最长n
def delete_min_parantheses(s: str) -> str:
    mapping = {
        ')': '(',
        ']':'[',
        '}': '{'
    }
    etr_open = collections.defaultdict(int)
    tot_open = collections.defaultdict(int)
    tmp = ""
    for i in range(len(s)):
        ch = s[i]
        if ch in mapping: # closing parentheses
            if etr_open[mapping[ch]] == 0:
                continue
            etr_open[mapping[ch]] -= 1  
            tmp += ch
        elif ch.isalnum():
            tmp += ch
        else: # opening parentheses
            etr_open[ch] += 1
            tot_open[ch] += 1
            tmp += ch
    net_open = collections.defaultdict(int)
    for key in tot_open:
        net_open[key] = tot_open[key] - etr_open[key]
    ret = ""
    for ch in tmp:
        if ch in tot_open:
            if net_open[ch] == 0:
                continue
            ret += ch
            net_open[ch] -= 1
        else:
            ret += ch
    return ret

# test
s1 = "[lee(t(c)o))))d[[e)(({{}}}"
s2 = "(((("
s3 = ")}"
print(delete_min_parantheses(s3))