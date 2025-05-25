from collections import Counter
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