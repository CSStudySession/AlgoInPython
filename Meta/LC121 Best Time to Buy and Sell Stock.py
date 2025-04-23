from typing import List
from collections import deque
# varinat1: given two arrays departures and returns where departures[i] and returns[i]
# are ticket prices for departing and returning flights on the ith day.
# to minimize the cost, we need to choose a single day to buy, and another day in future
# to return. Return the min-cost we can get for a single round-trip.
# e.g. dep: [1,2,3,4] rtn: [4,3,2,1] output:2. dep at idx 0, rtn at idx 3.
# to clarify:
# 1. whether the lengths of both given arrays are equal or not, if not given?
# 2. possible negative flight tickets, floating point values and overflow?

'''
思路: loop from left to right of rtn[], and maintain a min_cost and a min_dep_cost.
'''
def find_min_cost(dep: List[int], rtn: List[int]) -> int:
    if not dep or not rtn:
        return 0

    min_dep_cost = dep[0] # 初始化第一个最便宜 后面可能更新
    min_tot_cost = float('inf')

    for i in range(1, len(rtn)): # i意义是给rtn[i]找最便宜的dep 并更新min_dep
        min_tot_cost = min(min_tot_cost, min_dep_cost + rtn[i])
        if dep[i] < min_dep_cost:
            min_dep_cost = dep[i]
    return min_tot_cost

# test
dep = [8,3,6,10]
rtn = [10,9,5,8]
#print(find_min_cost(dep, rtn))

# varint2: return min-cost within k days: must arrive and depart within k days.
# 思路: Monotonic Queue来维护departures[i]在窗口[i - k, i - 1]中的最小值
# 1.初始化一个双端队列，用于维护一个单调递增的下标队列
# 2. 遍历每一个可能的返回日 r从第1天开始
# 3. 确保队列中只保留 [r - k, r - 1] 范围的出发日
# 4. 每次更新当前最小出发价 dep[d] 和当前 dep[d] + rtn[r]
# T(n):每个元素最多入队出队一次  S(k):队列中最多k个元素
def find_min_cost_within_k_days(dep:List[int], rtn:List[int], k:int) -> int:
    if not dep or not rtn:
        return 0
    queue = deque()
    min_tot_cost = float('inf')
    for i in range(1, len(rtn)):
        # 队列中只保留[i-k, i-1]天范围的dep下标 队头元素<i-k就出范围了
        while queue and queue[0] < i - k:
            queue.popleft() 
        d = i - 1
        # 当前出发日入队 维持队列单调增 队尾剔除>=当前的
        while queue and dep[queue[-1]] >= dep[d]:
            queue.pop()
        queue.append(d) # 只加一个新的d 因为窗口滑动会动态更新
        dep_min = dep[queue[0]] # 注意queue里存的是dep的下标
        min_tot_cost = min(min_tot_cost, dep_min + rtn[i])
    return min_tot_cost

# test
dep = [1, 2, 3, 4]
rtn = [4, 3, 2, 1]
k = 3
print(find_min_cost_within_k_days(dep, rtn, k))  # 输出 2（dep[0] + rtn[3]）