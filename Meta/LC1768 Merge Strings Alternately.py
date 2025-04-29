
# 双指针. i,j交替把当前的字符填入ret. 注意循环中的指针条件
# T(m+n) S(1) if we don't count ret
def mergeAlternately(word1, word2):
    m = len(word1)
    n = len(word2)
    i = 0
    j = 0
    ret = []

    while i < m or j < n: # 注意这里是or
        if i < m: # 因为上面用or 这里要判断是否越界
            ret += word1[i]
            i += 1
        if j < n:
            ret += word2[j]
            j += 1
    return "".join(ret)