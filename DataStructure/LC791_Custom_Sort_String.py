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