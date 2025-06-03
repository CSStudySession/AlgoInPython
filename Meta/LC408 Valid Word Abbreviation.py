'''
思路: 两个指针 i 和 j 分别指向 word 和 abbr 的当前位置；
- 如果abbr[j]!= word[i]
  - abbr[j]是0或者不是数字 返回False 因为不允许leading zeros或者无法跳过当前i
  - 如果abbr[j]是数字 连续读取abbr中的数字 转成整数num
    指针 i 在 word 中跳过 num 个字符:i += num
- 如果i,j对应元素相等 指针各进一步
最后判断两个指针是否都恰好走到字符串结尾: i == len(word) 且 j == len(abbr)
T: O(n)  S: O(n) for tmp字符串构建
代码也能handle word中有数字的情况.
'''
def validWordAbbreviation(word: str, abbr: str) -> bool:
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if word[i] != abbr[j]:
            if abbr[j] == '0' or not abbr[j].isdigit(): # if允许前导0 这里改成只有if not a[j].isdigit()就好 
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

'''
原题followup 1: 如果i18n中的18, 可以代表18, 或者1和8。
思路:DFS + memoization 来尝试所有可能的数字分割方式
步骤如下：
定义状态：使用两个指针 i 和 j 分别表示当前遍历到 word 和 abbr 的位置。
终止条件：
如果 i == len(word) 且 j == len(abbr)，说明完全匹配。
如果 i > len(word) 或 j >= len(abbr)，说明越界或未完全匹配，返回 False。
递归逻辑：
如果 abbr[j] 是字母，必须逐个匹配。
如果是数字（且不能以 '0' 开头），尝试所有可能的数字段（如 '12' 可以是 '1' 或 '12'），分别尝试跳过对应个数的字符。
优化：使用 memo[(i, j)] 存储状态避免重复计算。
T(n * m²)，其中 n 是 word 长度, m 是 abbr 长度。
因为每个位置都可能枚举多个数字段（例如 "123" 可以是 1, 12, 123) 加上记忆化避免重复路径。
S(n * m)，用于 memo.
'''
def validWordAbbreviationFlexible(word: str, abbr: str) -> bool:
    memo = {}
    return dfs(word, abbr, 0, 0, memo)

def dfs(word: str, abbr: str, i: int, j: int, memo: dict) -> bool:
    # 如果这个状态已经算过了，直接返回缓存结果
    if (i, j) in memo:
        return memo[(i, j)]
    # 两个指针都到达末尾，说明匹配成功
    if i == len(word) and j == len(abbr):
        return True
    # 超出范围，匹配失败
    if i > len(word) or j >= len(abbr):
        return False
    # 当前是字母，必须逐个匹配
    if abbr[j].isalpha():
        if i < len(word) and word[i] == abbr[j]:
            memo[(i, j)] = dfs(word, abbr, i + 1, j + 1, memo)
            return memo[(i, j)]
        else:
            memo[(i, j)] = False
            return False
    # 当前是数字段开头
    if abbr[j].isdigit():
        # 不允许 leading zero
        if abbr[j] == '0':
            memo[(i, j)] = False
            return False
        # 枚举所有可能的数字段（从 abbr[j] 开始向右扩展）
        for k in range(j, len(abbr)):
            if not abbr[j:k + 1].isdigit():
                break
            num = int(abbr[j:k + 1])
            # 尝试跳过 num 个字符，看剩下的是否能匹配
            if dfs(word, abbr, i + num, k + 1, memo):
                memo[(i, j)] = True
                return True
        memo[(i, j)] = False
        return False
    # 其他情况（非法字符）直接失败
    memo[(i, j)] = False
    return False

'''
followup 2: 如果1 and 8 可能不代表数字 就是普通的和 letter 一样的内容?
状态定义 dfs(i, j) 表示从 word[i:] 和 abbr[j:] 开始，是否能成功匹配。
遇到字母时，逐字符匹配。
遇到数字时：
 - 尝试将其作为字面数字，进行逐字符匹配。
 - 或者将连续数字解释为缩写数量，跳过对应字符 需判断 leading zero
用 memo[(i, j)] 记录中间状态，避免重复递归。
T(n*m^2) n = len(word), m = len(abbr). S(m*n) from memo. stack most S(m+n)
'''
def validWordAbbrFlexible(word: str, abbr: str) -> bool:
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(word) and j == len(abbr):
            return True
        if i > len(word) or j >= len(abbr):
            return False

        # abbr[j] 是字母
        if abbr[j].isalpha():
            if i < len(word) and word[i] == abbr[j]:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]
            memo[(i, j)] = False
            return False

        # abbr[j] 是数字
        # case 1：数字作为字面量匹配
        if i < len(word) and word[i] == abbr[j]:
            if dfs(i+1, j+1):
                memo[(i, j)] = True
                return True
        # case 2：数字作为缩写
        if abbr[j] == '0':  # leading zero 不合法
            memo[(i, j)] = False
            return False
        k = j
        while k < len(abbr) and abbr[k].isdigit():
            k += 1
        num = int(abbr[j:k])
        if dfs(i + num, k):
            memo[(i, j)] = True
            return True

        memo[(i, j)] = False
        return False
    return dfs(0, 0)

print(validWordAbbrFlexible("i18n", "i18n"))   # True: 18是缩写
print(validWordAbbrFlexible("i18n", "i1n"))    # False
print(validWordAbbrFlexible("abc", "a1c"))    # True