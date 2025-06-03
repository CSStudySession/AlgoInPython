'''
variant: 返回一个str str为合法分割的一个组合 词中间用空格分开.
e.g.: s = "applepenapple" word_bank = ["apple","pen"]  output: 'apple pen apple'
思路:dfs+memo. dfs尝试每种切分方式 并记录每个dfs层尝试切分的结果
每层找到一个可行解就返回
dfs函数:从位置start开始 对s进行DFS分词 返回可行的分词结果 (带空格)
- 若无解则返回None
T(n^2):n个切分起点 尝试所有end[start+1, n]  S(n^2): memo[0]:n m[1]:n-1 ... 1
一共:1+2+..+n ~=S(n^2)
'''
def word_break(s: str, wordDict: list[str]) -> str:
    wordSet = set(wordDict)               # 将列表转为哈希集合，快速查找
    memo = [None] * (len(s) + 1)          # 记忆化数组，存储从各位置开始的分词结果
    res = dfs(s, wordSet, 0, memo)
    return res if res is not None else ""  # None 则说明无解 返回空字符串

def dfs(s: str, wordSet: set, start: int, memo: list[str]) -> str:
    # 已经处理过start位置 直接返回结果
    if memo[start] is not None:
        return memo[start]
    # 到达字符串末尾 说明前面都能成功分词
    if start == len(s):
        return ""  # 空字符串表示已经分完 不需要再加词
    for end in range(start + 1, len(s) + 1):  # 尝试所有可能的切分位置
        word = s[start:end]
        if word in wordSet: # 如果当前子串在字典中 则继续搜索下一个位置
            rest = dfs(s, wordSet, end, memo)
            # 如果后续能成功分词(包括空字符串):组装结果并返回
            if rest is not None:
                # 若rest为空 说明正好切到末尾 不额外加空格
                result = word + ("" if rest == "" else " " + rest)
                memo[start] = result
                return result
    # 所有切分都不行 标记无解
    memo[start] = None
    return None

s = "qwerasdf"
word_bank = ["asdf","qwer"]
#s = "applepenapple"
#word_bank = ["apple","pen"]
#s = "catsandog"
#word_bank = ["cats","dog","sand","and","cat"] # empty
print(word_break(s, word_bank))
