'''
思路:二分
- 要找船的最小容量 范围:max(weights)到sum(weights)之间
设定左边界l=max(weights) 右边界r=sum(weights)
在区间[l, r]上二分 mid=(l + r) // 2 判断以容量mid时 是否能够在不超过days天内运完包裹
如果可以 说明答案可能更小 将右边界收缩为mid 否则左边界移到mid + 1
最终 r or l 即为所求最小容量
- 可行性检查 check_valid:
从第一天开始累加包裹重量 若超过当前容量limit 则开启新的一天need+=1 并将当天已装重量重置为当前包裹重量
遍历结束后 若所需天数need不超过给定的days 则说明容量limit可行
T(nlog(r-l)) S(1)
'''
def shipWithinDays(weights: list[int], days: int) -> int:
    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if check_valid(weights, mid, days): # mid满足条件 可能是解 可以尝试更小的
            right = mid
        else: # mid一定不是解
            left = mid + 1
    return right

def check_valid(weights:list[int], limit:int, days:int) -> bool:
    need, cur_w = 1, 0 # need从1开始 下面累加w到超出limit时 直接+=1
    for w in weights:
        if w > limit:
            return False
        if cur_w + w > limit:
            need += 1
            cur_w = w # 当前的w要留给下一天carry
        else:
            cur_w += w
    return need <= days # 注意要跟days比大小