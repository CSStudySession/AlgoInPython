'''
Part 1:找出日志中出现频率最高的 k 个广告
输入: 一个静态日志文件(log file) 每一行包含:
  - 广告名称：如 ads_1
  - 时间戳：如 1595268625

输出: 调用getCommonAds(k) 返回频率最高的 k 个广告名
Clarifications
总共最多有 10 万个 unique ads(例如 100,000)
如果内存不够，可以讨论分布式方案
如果频率相同是否要打破tie? 由面试官决定.
part1思路: min heap求top k
'''
import heapq
from collections import defaultdict
def get_common_ads(log_data, k):
    freq_map = defaultdict(int)
    for ad_name, _ in log_data:
        freq_map[ad_name] += 1
    # 使用最小堆存储前K个频率最高的广告
    min_heap = []
    for ad, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, ad))
        elif min_heap[0][0] < freq:
            heapq.heappushpop(min_heap, (freq, ad))
    return min_heap

'''
part2: 支持时间窗口的 top-k 广告统计
需求:只统计当前时间向前1小时内的ad impressions(sliding window)
函数接口:ingestImpression(impression): 不断地流式接入impression(广告+时间戳)
getCommonAds(k)：获取最近 1 小时内的 top-k 广告

Clarifications
流式实时接入 数据无序但每次window是1小时
ingestImpression 和 getCommonAds 调用次数大致相等
思路:
维护两个dict 一个queue 一个当前时间(因为ads是out of order来的)
freq_map: ad to freq/cnt
cnt map: cnt to a set of ads. 用sortedDict key从高到低排序
每次来一个新的ad 更新两个maps和在队列中移除时间过期的ads
'''
from collections import deque, defaultdict
from sortedcontainers import SortedDict  # pip install sortedcontainers

class SlidingTopK:
    def __init__(self):
        self.window = deque()  # 存储 (timestamp, ad)
        self.freq_map = defaultdict(int)  # ad -> count
        self.count_map = SortedDict()     # count -> set of ads，频率从低到高排序
        self.cur_time = 0

    '''
    维护一个sliding window(滑动窗口)中最近1小时的广告 并实时更新频率统计结构
    以便快速获取top-k广告
    用sortedDict 查找/删除 都是logM, M是dict中key的数量. 清理过期ads可能会出现 时间推进了
    一大截 窗口内ads都过期: T(w*logM). 但amertized看 大概在~T(logM) S(w(ads num) + n(freq))
    '''
    def ingest_impression(self, ad, timestamp):
        self.cur_time = max(self.cur_time, timestamp) # 更新当前时间 数据out-of-order到达
        self.window.append((timestamp, ad)) # 更新time window
        # 更新ad->freq dict
        prev_count = self.freq_map[ad]
        self.freq_map[ad] += 1
        new_count = self.freq_map[ad]

        if prev_count > 0: # 取出旧的freq对应的set 扔掉ad 如果set空了 删掉set
            ad_set = self.count_map.get(prev_count)
            ad_set.discard(ad)
            if not ad_set:
                del self.count_map[prev_count]
        # setdefault(key, xx) key存在 则返回对应val, 不存在 则返回default xx
        self.count_map.setdefault(new_count, set()).add(ad)

        # 移除过期 impression
        expire_time = self.cur_time - 3600
        while self.window and self.window[0][0] < expire_time:
            _, old_ad = self.window.popleft()
            old_count = self.freq_map[old_ad]

            self.count_map[old_count].discard(old_ad)
            if not self.count_map[old_count]:
                del self.count_map[old_count]

            self.freq_map[old_ad] -= 1
            if self.freq_map[old_ad] == 0:
                del self.freq_map[old_ad]
            else:
                new_count = self.freq_map[old_ad]
                self.count_map.setdefault(new_count, set()).add(old_ad)
    # 遍历cnt_map:T(M)(sortedDict遍历key是线性时间复杂度), 内部循环O(k) -> T(M+k)
    def get_common_ads(self, k):
        result = []
        # 倒序遍历频率（从高到低）
        for freq in reversed(self.count_map):
            for ad in self.count_map[freq]: # 可以不排序 要求的话加一个sorted(cnt_map)
                result.append(ad)
                if len(result) == k:
                    return result
        return result
    
'''
part3 某些广告impression的arrival会延迟(即窗口中数据不是实时到达的)
仍需支持getCommon(k)获取当前 top-k 广告
函数接口:
ingestImpression(impression)：插入一个广告 impression(名称 + 时间戳)
getCommon(k):返回当前最常见的k个广告名(即使数据延迟到达)
思路:因为数据可能延迟 不能直接用window 只能基于完整历史进行频率维护
解法与Part 2类似 但不做过期清理
数据结构:两个map
freq_map: ad_name → count
count_map: count → set of ad_names
'''
from collections import defaultdict
from sortedcontainers import SortedDict  # pip install sortedcontainers

class TopKImpression:
    def __init__(self):
        self.freq_map = defaultdict(int) # ad → count
        self.count_map = SortedDict()    # count → set of ads
    # T(logm)
    def ingest_impression(self, ad):
        prev_count = self.freq_map[ad]
        self.freq_map[ad] += 1
        new_count = self.freq_map[ad]

        if prev_count > 0:
            ad_set = self.count_map.get(prev_count)  # 通过旧cnt找到旧set
            ad_set.discard(ad)                       # 从旧set中移除当前ad
            if not ad_set:                           # set空了 就删掉
                del self.count_map[prev_count]
        # 把ad放到 new cnt对应的set
        self.count_map.setdefault(new_count, set()).add(ad)
    # T(m+k)
    def get_common(self, k):
        result = []
        for freq in reversed(self.count_map):  # 从高频到低频遍历
            for ad in self.count_map[freq]:    # 如果不要求字典序可省略 sorted()
                result.append(ad)
                if len(result) == k:
                    return result
        return result

'''
followup:
如何找出最少频率的广告？
getCommon(k)的遍历方向为正序(从最小频率开始)
'''