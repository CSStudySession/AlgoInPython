'''
varint: Return all the longest contiguous substrings of repeated characters. 
If there are multiple substrings with the same maximum length, return all of them.
输入: s = "aabbbccdddbbb"
输出: ["bbb", "bbb", "ddd"]
思路:
- 遍历字符串 记录每段连续子串 用变量max_len记录当前最长长度
- 用一个结果列表res保存最长的子串
  - 如果当前子串长度等于max_len加入结果
  - 如果当前子串长度更大 则更新max_len 并清空结果后加入当前子串
T(n) S(1)
'''
def all_longest_repeating_substrings(s: str) -> list:
    if not s:
        return []
    res = []  # 存储所有最长连续重复子串
    max_len = 1
    cur_len = 1
    start = 0  # 当前连续子串的起始位置

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            if cur_len == max_len:
                res.append(s[start:i])  # 同样是最长，加入
            elif cur_len > max_len:
                max_len = cur_len
                res = [s[start:i]]  # 更长，更新结果
            cur_len = 1
            start = i
    # 处理最后一段 或者长度为1的str根本没进循环 
    if cur_len == max_len:
        res.append(s[start:])
    elif cur_len > max_len:
        res = [s[start:]]
    return res

s = "aabbbccdddbbbaaa"
# s = 'a'
print(all_longest_repeating_substrings(s))


'''
lc orign.
思路:两个变量max_len和cur_len 分别表示当前最大连续字符长度 和 当前字符的连续长度
遍历字符串 如果当前字符等于前一个字符 就把cur_len加 1 否则重置为1
每次都更新max_len= max(max_len, cur_len)。
最终返回max_len
T(n) S(1)
'''
def max_power(s: str) -> int:
    if not s:
        return 0
    max_len = 1  # 最长连续长度至少为1
    cur_len = 1  # 当前字符连续长度
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cur_len += 1
        else:
            cur_len = 1  # 遇到不同字符就重置
        if cur_len > max_len:
            max_len = cur_len  # 更新最大长度
    return max_len