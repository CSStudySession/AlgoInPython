'''
给定: 一个整数 K, 表示最多可停留的夜晚数(即最多可将路径分为 K+1 段)
一个非递减列表T, 表示途经的地理位置坐标(从起点 T[0] 到终点 T[-1]) 例如海拔或距离
目标是找出一种分段方式(在某些点停留) 使得所有天数中的最长单日路程尽可能小

翻译一下:
在停留K晚的前提下, 把T分为K+1段 使得: 所有段中“最长的一段的长度(最大单日路程)”最小

思路:二分
1. 确定搜索空间：最长单日路程的范围在 [max_diff, total_dist] 之间。
- max_diff: 任意两个相邻地点之间的最大差值
- total_dist: T[-1] - T[0]
2. Binary Search on Answer
设 mid 为当前尝试的最长单日路程 检查是否可以在K个停留点内完成。
检查方式: 从起点出发 尽量走<= mid的最长距离 记录分段数是否 ≤ K+1
3. 贪心检查函数(Greedy Check) 这个helper用在binary search中
每次尽可能走当前允许的最大距离<= mid 并统计用了多少段.
T(nlog(max_diff)) S(1)
'''
def min_longest_day_hike(k: int, T: list[int]) -> int:
    if not T:
        return 0
    def can_partition(max_day: int) -> bool: # helper
        count, last = 0, T[0]
        for i in range(1, len(T)):
            if T[i] - last > max_day:
                count += 1
                last = T[i-1]
        return count <= k

    left = max(T[i+1] - T[i] for i in range(len(T)-1)) # 求最大的相邻diff
    right = T[-1] - T[0] # 二分的upper bound:直接一天内跑完所有路径
    while left < right:
        mid = (left + right) // 2
        if can_partition(mid): # mid可能是答案 可以尝试更小的mid
            right = mid
        else:
            left = mid + 1
    return left

assert(min_longest_day_hike(1, [0, 4, 7, 11, 12]) == 7)

'''
followup1: 已知最优最长单日路程为D, 求在哪些点停留?
思路: 按照D做一次贪心遍历 只要当前位置距离上次停留点超过D, 就记录停留在前一个点
'''
def determine_stops(max_day: int, T: list[int]) -> list[int]:
    stops = []
    if not T or max_day <= 0: # sanity check
        return stops
    last = T[0]
    for i in range(1, len(T)):
        if T[i] - last > max_day:
            stops.append(T[i-1])
            last = T[i-1]
    return stops

'''
followup2: 如果 T 是 list[float] 怎么做？
思路: 二分 唯一变化是:二分搜索不再是整数范围 而是对浮点数进行搜索
更改方式：
使用 epsilon = 1e-6 控制二分精度, 检查条件为 right - left > epsilon。
注意: 比较浮点数时避免直接用 ==, 使用小数差值判断是否“足够接近”
T(nlog(max_diff)) S(1)
'''
def min_longest_day_hike(k: int, T: list[float]) -> float:
    if not T:
        return 0.0
    def can_partition(max_day: float) -> bool:
        count, last = T[0]
        for i in range(1, len(T)):
            if T[i] - last > max_day:
                count += 1
                last = T[i-1]
        return count <= k
    left = max(T[i+1] - T[i] for i in range(len(T)-1))  # 每天至少得走的最远一步
    right = T[-1] - T[0]  # 最多一天全走完
    epsilon = 1e-6
    while right - left > epsilon:
        mid = (left + right) / 2.0
        if can_partition(mid):
            right = mid
        else:
            left = mid
    return left
