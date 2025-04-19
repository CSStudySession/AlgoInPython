# Return city name depending on their probability
# example: list[[Boston, 1] [New York, 2][Los Angeles,1]]
# if you call getCity() --> it should return New York 50% of the time not more than that
# other two 25% of the time.
# ref LC528: https://leetcode.com/problems/random-pick-with-weight/description/
import random

def getCity(cities):
    presum = [0] * len(cities)
    presum[0] = cities[0][1]
    for i in range(1, len(cities)):
        presum[i] = cities[i][1] + presum[i - 1]
    total = presum[-1]
    # print(presum)

    # find the first index in prefix that >= target: binary search 
    # 在prefix里搜索第一个比target大的数的(index)
    # eg [1,3], prefix区间为[0,1) [1,4) target在两个区间的比例为25%, 75%
    target = random.randint(1, total)
    left, right = 0, len(presum) - 1
    while left < right:
        mid = (left + right) // 2
        if presum[mid] < target:
            left = mid + 1
        else:
            right = mid
    return cities[left][0]

cities = [["Boston", 1],["New York", 2],["Los Angeles", 1]]
print(getCity(cities))