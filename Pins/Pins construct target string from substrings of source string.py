from collections import defaultdict
'''
给定一个source字符串和一个target字符串 可以多次使用source字符串的副本 并从中移除任意字符 目标是构造出完整的target字符串。
要求：
Part A: 判断是否可以构造出target字符串 返回 True/False 
Part B: 如果可以构造 返回最少需要多少次使用source字符串的副本来构造出target字符串。
Part C: 优化 Part B 的解法，降低时间复杂度。

思路
part A
因为每次都可以“移除字符”，所以只要 source 中包含 target 的所有字符即可。
把 source 字符放到 set 里去重（查找更快）。
遍历 target 的字符，逐一在 source_set 中查是否存在。
全部存在就返回 True 否则 False。
part B
如果 Part A 判定不能构造，直接返回 0。
用两个指针：一个指向 target(当前要匹配的字符) 一个从头遍历 source。
每次遍历 source, 尝试尽量匹配 target 的连续字符（顺序不能乱）。
匹配一轮后(走完整个 source), count +1  再从 source 头部继续匹配 target 剩下部分。
重复上面过程，直到 target 被完全匹配完
PartC
先构建一个映射：每个字符 -> 它在 source 中出现的所有位置（升序列表）。
例如source = "abcab"，构建出：
{
  'a': [0, 3],
  'b': [1, 4],
  'c': [2]
}
从 target 开始遍历：
每次在当前字符的索引列表中，二分查找第一个大于当前指针的位置，表示当前副本能否继续用。
如果找不到，就换新的副本(计数 +1) 从字符在 source 中的第一个位置开始继续。
遍历 target 完成后，统计用了多少次副本
'''
# part A. return if it can be created. True or False  T(m + n) S(m + n)
def can_create(source: str, target: str) -> bool:
    source = source.lower()
    target = target.lower()
    # 把 source 中所有字符放入一个 set 里（去重 + 快速查找）
    source_set = set()
    for c in source:
        source_set.add(c)
    # 遍历 target 的每个字符，看是否都在 source_set 中
    for c in target:
        if c not in source_set:
            return False  # 有一个找不到就直接返回 False
    return True  # 所有字符都找到了

# Part B  T(m * n) S(m + n) lower()产生了两个临时字符串
def count_copies(source: str, target: str) -> int:
    if not can_create(source, target):
        return 0
    source = source.lower()
    target = target.lower()
    count = 0
    i = 0  # pointer in target
    while i < len(target):
        j = 0  # pointer in source
        # 匹配 source 中能覆盖的最大部分 target
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
        count += 1  # 每次使用一个 source 副本
    return count

# Part C T(m + n*logm) S(m + n)
def count_copies_bs(source: str, target: str) -> int:
    if not can_create(source, target):
        return 0
    source = source.lower()
    target = target.lower()
    # Step 1: 构建 source 中每个字符出现的所有位置（升序列表）
    char_index = defaultdict(list)
    for idx, char in enumerate(source):
        char_index[char].append(idx)
    cnt = 1  # 至少要用一次 source 副本
    pos_in_src = -1  # 当前正在匹配的 source 索引位置
    for char in target:
        indices = char_index[char]
        # 用 bisect 在 indices 中查找第一个 > pos_in_source 的索引
        i = binary_search(indices, pos_in_src)
        if i == -1:
            # 没找到 说明要用一个新的source副本
            cnt += 1
            pos_in_src = indices[0]
        else:
            # 找到了 更新当前位置
            pos_in_src = indices[i]
    return cnt

def binary_search(indices, pos_in_src): # 在indices中找第一个大于pos_in_src的元素 返回其下标
    if not indices:
        return -1
    left, right = 0, len(indices) - 1
    while left < right:
        mid = (left + right) // 2
        if indices[mid] > pos_in_src:
            right = mid
        else:
            left = mid + 1
    return right if indices[right] > pos_in_src else -1

assert count_copies_bs("aba", "baba") == 2
assert count_copies_bs("ap", "papa") == 3
assert count_copies_bs("aba", "aa") == 1