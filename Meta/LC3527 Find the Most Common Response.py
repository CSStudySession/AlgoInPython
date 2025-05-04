import collections
'''思路:遍历+去重+遍历比较
1.去重每一天的回答.由于同一天中同一个回答可能出现多次 但只应算一次 需要对每天的回答先使用集合set去重
2.统计所有回答的频率.遍历所有天的去重后的回答用dict统计每个回答出现的次数
3.找出出现次数最多的回答：遍历统计结果，记录最大频率
  -- 字典序处理:如果有多个回答出现次数相同 选择字典序最小的那一个作答案
T(n) S(n) n is num of unique words 
'''
def findCommonResponse(responses: list[list[str]]) -> str:
    if not responses:
        return ''
    resp_to_cnt = collections.defaultdict(int)
    for response in responses:
        unique = set(response)
        for item in unique:
            resp_to_cnt[item] += 1
    max_cnt = max(resp_to_cnt.values()) # values()代表次数
    ret = ''
    for word, cnt in resp_to_cnt.items():
        if cnt == max_cnt:
            if ret == '' or ret > word: # 字符串直接按字典序比大小
                ret = word
    return ret