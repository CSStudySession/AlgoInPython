import collections

# lc original. 先计算s的counter 再按照order的顺序逐个append to res,最后加上剩余counter里面的
# meta varint: given a list of char as "order" instead of str, 或者不说什么input形式,需要自己问.
def customSortString(order: str, s: str) -> str:
    if not order or not s:
        return ""
    ch_to_freq = collections.Counter(s)
    ret = []
    for char in order:
        while ch_to_freq[char] > 0:
            ret.append(char)
            ch_to_freq[char] -= 1
    for char, freq in ch_to_freq.items():
        ret.append(char * freq)
    return ''.join(ret)

# followup: how to optimize the above solution?
# instead using dict which could have hash collision issues, use list to store frequence.
# map each of letter to an index of a list with length 26.
# T(max_len(order, s))  S(1)辅助数组长度为26->常数
def customSortString_vec(order: str, s: str) -> str:
    if not order or not s:
        return ""
    ch_to_freq = [0] * 26 # 26个字母在s中出现的频率
    for char in s:
        idx = ord(char) - ord('a')
        ch_to_freq[idx] += 1
    
    ret = ""
    for char in order:
        idx = ord(char) - ord('a') # 注意这里要算出char对应的下标
        if ch_to_freq[idx] != 0:
            ret += ch_to_freq[idx] * char
            ch_to_freq[idx] = 0
    for i in range(len(ch_to_freq)):
        if ch_to_freq[i] != 0:
            ret += ch_to_freq[i] * chr(i + ord('a'))
    return ret

'''
variant: what if input has both upper and lower cases?
1. 如果“不忽略大小写”自定义排序 没影响
2. 如果“忽略大小写”自定义排序
需要做预处理: 统一大小写
 -先把order和s都.lower() 再做统计和排序
 -排序完后 如果需要保留原始大小写形式 要再多做一次“映射回去”的工作
'''
# 1. 先把 s 里所有字符按 lower() 统计频次，同时记下每个原字符的列表
def custom_sort_case_sensitive(order: str, s: str) -> str:
    lower_freq = collections.Counter(ch.lower() for ch in s)
    original_map = collections.defaultdict(list)
    for ch in s:
        original_map[ch.lower()].append(ch)
    # 2. 按 order.lower() 排序
    ret = []
    for ch in order.lower():
        while lower_freq[ch] > 0:
            # 从 original_map 里拿出一个原形式（可能是大写也可能小写）
            ret.append(original_map[ch].pop())
            lower_freq[ch] -= 1
    # 3. 剩余的也按相同方式回写
    for ch_lower, freq in lower_freq.items():
        while freq > 0:
            ret.append(original_map[ch_lower].pop())
            freq -= 1
    return ''.join(ret)