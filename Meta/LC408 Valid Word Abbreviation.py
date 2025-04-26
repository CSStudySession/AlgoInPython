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

# variant: what if abbreviation can have wildcards?
'''
- 使用递归函数 recurse(word, abbr, w, a) 表示: 
当前在 word 的第 w 个位置, 当前在 abbr 的第 a 个位置 尝试判断后续是否可以合法匹配
- 递归处理逻辑 终止条件:
w == len(word) 且 a == len(abbr) → 成功匹配
a == len(abbr) 但 w < len(word) → 失败
w == len(word) 但 a < len(abbr) → 如果 abbr 剩下的全是 *，则合法；否则不合法。
- 处理数字：
连续读取数字字符 组合成要跳过的长度skip 然后在word上跳过相应字符继续递归
- 处理通配符* 两种选择:
* 匹配空串 recurse(word, abbr, w, a+1)
* 匹配当前字符 recurse(word, abbr, w+1, a)
- 处理字母:如果当前字母一致 继续递归
否则匹配失败
T(n * m)（每个状态最多访问一次） S(n * m) memo和递归栈
'''
def validWordAbbreviationWithWildCard(word: str, abbr: str) -> bool:
    memo = {}
    return recursion(word, abbr, 0, 0, memo)

def recursion(word:str, abbr:str, w:int, a:int, memo:dict) -> bool:
    key = (w,a)
    if key in memo:
        return memo[key]
    if w == len(word) and a == len(abbr):
        memo[key] = True
        return True
    if a == len(abbr):
        memo[key] = False
        return False
    if w == len(word):
        for i in range(a, len(abbr)):
            if abbr[i] != "*":
                memo[key] = False
                return False
        memo[key] = True
        return True
    if abbr[a].isdigit(): # a指向数字 w跳过对应的数字个数
        if abbr[a] == '0':
            memo[key] == False
            return False
        skip, k = 0, a
        while k < len(abbr) and abbr[k].isdigit():
            skip = skip * 10 + int(abbr[k])
            k += 1
        if w + skip > len(word):
            memo[key] = False
            return False
        memo[key] = recursion(word, abbr, w + skip, k, memo)
        return memo[key]
    if abbr[a] == '*': # 通配符 可以匹配空 可以匹配当前
        match_empty = recursion(word, abbr, w, a + 1, memo)
        match_one = recursion(word, abbr, w + 1, a, memo) if w < len(word) else False
        memo[key] = match_empty or match_one
        return memo[key]
    if word[w] == abbr[a]:
        memo[key] = recursion(word, abbr, w + 1, a + 1, memo)
        return memo[key]
    memo[key] = False # w,a均指向普通字符 但字符不相等
    return False