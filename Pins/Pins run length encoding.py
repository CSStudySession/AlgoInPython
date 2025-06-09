'''
给定一个包含重复字符的字符串，例如 "aaabbdcccaaaa"，实现一个编码函数，
将连续重复的字符以“字符重复次数+字符”的形式输出。
例如：
输入: "aaabbdccca"
输出: "3a2b1d3c1a"
输入：一个字符串 s 由任意字符组成 (ASCII 或非 ASCII)
输出：将字符串进行 Run-Length Encoding 压缩后的字符串
Clarifications
问题很直接，不需要特别的数据结构或性能优化技巧

思路:
1. 遍历字符串，维护当前字符及其出现次数
2. 若遇到不同字符，输出上一个字符及其累计次数
3. 继续记录新字符
4. 注意处理字符串末尾字符的计数
T(n) S(n)
'''
def run_length_encode(text):
    if not text:
        return ""
    result = []
    prev_char = text[0]
    cnt = 1
    for ch in text[1:]:
        if ch == prev_char:
            cnt += 1
        else:
            result.append(f"{cnt}{prev_char}")  # 添加上一个字符的计数
            prev_char = ch
            cnt = 1
    result.append(f"{cnt}{prev_char}")  # 处理最后一个字符
    return "".join(result)

assert(run_length_encode("a") == "1a")
assert(run_length_encode("ab") == "1a1b")
assert(run_length_encode("aba") == "1a1b1a")
assert(run_length_encode("😊😊😊😢") == "3😊1😢")