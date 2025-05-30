from collections import deque
# return all Strobogrammatic Number with lenth n
'''
思路1:dfs
对于长度n 递归构造从内到外的合法数
  - 定义字符串中心 n为奇数时 中心只能为 '0','1','8'
  - 外层递归时 拼接合法的字符对（如 '6'-'9'）在当前结果两端
  - 最外层不能以'0'开头 除非n==1
T(n*5^(n/2)) S(5^(n/2)) (at most N/2 dfs calls, prev stores temp results and takes space)
'''
def findStrobogrammatic_dfs(n: int) -> list:
    # 中心字符（n为奇数时）
    mid_cdds = ['0', '1', '8']
    # 对称字符对
    pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    return build(n, n, pairs, mid_cdds)

def build(k, final_len, pairs, mid_cdds) -> list:
    if k == 0:
        return ['']
    if k == 1:
        return mid_cdds
    prev = build(k - 2, final_len, pairs, mid_cdds) # 每次生成两位数 故-2
    result = []
    for s in prev:
        for a, b in pairs:
            # 首字符不能是0（除非整体长度是1）
            if k == final_len and a == '0':
                continue
            result.append(a + s + b)
    return result

'''
思路2:bfs
将字符串生成过程看作一个「层层扩展」的过程 用Queue进行BFS
初始化：如果 n 是奇数，初始队列为：["0", "1", "8"], 如果 n 是偶数，初始队列为：[""]
每次从队列中取出一个字符串 s, 然后将一组合法的字符对 a + s + b 加回队列 直到字符串长度为 n
最外层不能加 '0' 开头 除非整个数字就是 '0' 其长度为1.
T(n*5^(n/2)) S(5^(n/2))
'''
def findStrobogrammatic_bfs(n: int) -> list:
    if n == 0:
        return []
    if n == 1:
        return ['0', '1', '8']
    # BFS初始状态
    queue = deque()
    if n % 2 == 0:
        queue.append("")  # 偶数长度，从空心开始扩展
    else:
        queue.extend(['0', '1', '8'])  # 奇数长度，中间必须是这三个数
    pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
    # 每次扩展两位，直到长度为n
    while queue and len(queue[0]) < n:
        size = len(queue)
        for _ in range(size):
            s = queue.popleft()
            for a, b in pairs:
                # 外层不能以'0'开头，除非是最内层（最终只剩一位或空串）
                if len(s) + 2 == n and a == '0':
                    continue
                queue.append(a + s + b)
    return list(queue)

'''
leetcode 246: Given a string num which represents an integer, return true if num is a strobogrammatic number.
思路: 观察得知 只有在映射表中的数字才满足要求: [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
使用左右双指针 判断每对字符是否在旋转映射表中能互相转化
遇到无法匹配的直接返回 False
T(n) S(1)
'''
def isStrobogrammatic(num: str) -> bool:
    mapping = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    left = 0
    right = len(num) - 1
    while left <= right:
        if num[left] not in mapping or num[right] not in mapping:
            return False
        # 左右字符旋转后必须一致
        if mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True