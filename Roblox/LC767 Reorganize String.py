from collections import Counter
import collections
'''
1.统计字符频率 统计字符串中每个字符出现的次数
2.判断是否可能重排 若某个字符的出现次数超过了 (len(s)+1)//2 则无法避免相邻重复 返回空字符串
3.优先放置高频字符 先将出现次数最多的字符放在下标为偶数的位置（间隔放置，避免相邻）
4.再放其他字符:按任意顺序将剩余字符继续间隔填充到偶数或奇数下标上
T(n) S(k) k是unique letter的个数 如果都是小写字母 可以看成O(1)
'''
def reorganizeString(s: str) -> str:
    char_counts = Counter(s)  # 统计每个字符出现的次数
    # 找出出现次数最多的字符
    max_count, letter = 0, ''
    for char, count in char_counts.items():
        if count > max_count:
            max_count = count
            letter = char
    # 如果最多的字符数量大于 (len(s)+1)//2，无法重排
    if max_count > (len(s) + 1) // 2:
        return ""
    ans = [''] * len(s)  # 结果数组
    index = 0  # 从偶数位开始放置字符
    # 先放置最多的字符，间隔放置
    while char_counts[letter] != 0:
        ans[index] = letter
        index += 2
        char_counts[letter] -= 1
    # 放置剩余的字符
    for char, count in char_counts.items():
        while count > 0:
            if index >= len(ans):
                index = 1
            ans[index] = char
            index += 2
            count -= 1
    return ''.join(ans)

'''
variant1: 变了说法
给定一个映射 x->x[i] 表示数字i出现的次数 将所有这些数字排成一排 要求相邻的数字不能相同
需要:
1. 判断是否存在这样的排列。
2. 如果存在，构造出一种可行排列
要求所有算法时间复杂度为 O(N) (不能用堆)
思路:
某个数字的出现次数不能超过 (N+1)//2, 否则肯定没法避免相邻相同
证明:如果一个数太多了 比如一半以上 那即使每隔一个插一次 也不够间隔开
'''
# 判断是否能arrange. T(n) S(1)
def can_rearrange(x:dict[int, int]) -> bool:
    total = sum(x.values())
    max_count = max(x.values())
    return max_count <= (total + 1) // 2

'''
构造一个数列
将最多的元素先填在偶数位 0, 2, 4, ... 然后填剩下的数 偶数位填满后再填奇数位
这样保证没有两个相同的数字相邻
步骤：
找出现次数最多的数字
按先偶数后奇数填充
T(n) S(n) if we count sorted()
'''
def construct_rearrange(x: dict[int, int]) -> list[int]:
    total = sum(x.values())
    res = [None] * total
    # 找出现次数最多的数字
    max_num = None
    max_count = 0
    for num, count in x.items():
        if count > max_count:
            max_num = num
            max_count = count
    # 先填最多的元素
    idx = 0
    for _ in range(max_count):
        res[idx] = max_num
        idx += 2
    # 更新该元素剩余次数
    x[max_num] = 0
    # 填其他元素
    for num, count in x.items():
        for _ in range(count):
            if idx >= total:
                idx = 1  # 偶数位填完，切换到奇数位
            res[idx] = num
            idx += 2
    return res

'''
variant2: 给定一个字符串数组games 每个元素代表一种game 可能有重复
需要重新排列这些元素 使得任意相邻的两个元素都不是同一个game
如果无法完成这样的重排 返回空列表 [] 或空字符串 ""
T(n) S(n)
'''
def rearrange_games(games):
    n = len(games)
    count = collections.defaultdict(int)
    max_game = None
    max_freq = 0
    # 统计次数并找出现最多的元素
    for g in games:
        count[g] += 1
        if count[g] > max_freq:
            max_freq = count[g]
            max_game = g
    if max_freq > (n + 1) // 2:
        return []
    res = [None] * n
    i = 0
    # 先填最多的元素
    for _ in range(max_freq):
        res[i] = max_game
        i += 2
    count[max_game] = 0
    # 再填其他元素
    for game, freq in count.items():
        for _ in range(freq):
            if i >= n:
                i = 1  # 偶数位填满，转到奇数位
            res[i] = game
            i += 2
    return res

# test
games = ['A', 'A', 'B', 'B', 'C']
print(rearrange_games(games))