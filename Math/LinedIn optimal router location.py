'''
let the distance between two 1-dim data points x_i and x_j, be defined as ||x_i - x_j||^2
given the location of N-houses on a number line, we would like to put 2 routers on the number line,
where each house is assgined only one router, such that the sum of distances of houses to the assgined router
is minimized.

constriants:
N >= 2, number of routers:2

example:
house locations: [4,8,12,18]  number of routers:2
output: 26

clarication questions:
1. house location integer? yes
2. house locations can be negative? yes
3. locations can be 2 or more dimentional? No. always 1 dim.
'''

from typing import List

def get_optimal_dist(houses: List[int]) -> float:
    if not houses:
        return 0.0
    length = len(houses)

    prefix_dist = generate_prefix_dist(houses)
    houses.reverse()
    suffix_dist = generate_prefix_dist(houses)
    suffix_dist.reverse()

    min_dist = float("inf")
    for i in range(1, length):
        cur_min = prefix_dist[i - 1] + suffix_dist[i]
        min_dist = min(min_dist, cur_min)
    return min_dist

def generate_prefix_dist(houses: List[int]) -> List[float]:
    ret = []
    sum, sqr_sum = 0.0, 0.0

    for idx in range(len(houses)):
        sum += houses[idx]
        avg = sum / (idx + 1)        # 下面展开的距离和公式用到
        sqr_sum += houses[idx] ** 2  # 下面展开的距离和公式用到
        # 前m个点构成的子数组 到均值点的距离之和: sum{i from 1:m}(x_i - x_avg)^2
        # 根据平方和公式展开: x_i ^ 2 + x_avg ^ 2 - 2*x_i*x_avg
        # 注意x_avg * 2这一项 与i无关 前m个求和 等于 m * (x_avg^2) 
        dist = sqr_sum + (idx + 1) * avg ** 2 - 2 * avg * sum

        ret.append(dist)
    return ret

houses = [4,8,12,18]
print(get_optimal_dist(houses))