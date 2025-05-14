import random
from typing import List, Optional
'''
https://leetcode.com/problems/random-pick-with-weight/

w:     [1, 2, 3]
idx:    0  1  2
随机返回一个下标 要求返回下标对应的权重 与总权重(每个权重相加)成正比
先把w的值想象成一个个线段:
 A  B    C 
<-><--><--->
  1   3    6
A,B,C三个区间长度分别为1,2,3 (1,3,6)是区间总长度 
假如现在有个[1,6]之间随机数 落在哪个区间上 就返回对应区间的下标即可
比如落在B区间 返回B区间对应的下标1 就符合下标对应的权重与总权重成正比
如何实现上述操作? 转化成整数二分+前缀和
观察到:(1,3,6)这几个区间长度的尾端点 就是w的前缀和
prefix sum: 0 1 2 3 4 5 6 (注意只有1,3,6是前缀和 其它数字写出来方便后续理解)
区间:        <-><--><---->         
区间编号:      A  B    C  
w idx:        0   1    2

问题转化为: 随机出一个[1,max_prefix_sum]之间的整数target 然后二分前缀和数组 
找到第一个大于等于target的值 等价于找到了这个随机数落在了哪个长度的区间内
二分找到的值 代表了所在区间长度的右端点 它的下标 也就是w原数组的下标 

测试方法: pick_index()加一个参数fix_target 默认是None 测试时 传入固定值 这样
结果也会固定
'''
class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]
    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1]) # 随机一个[1, max_prefix_sum]之间的整数
        # 二分找第一个大于等于target的前缀和的值 并返回对应的下标
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target: # mid对应的值比target小 一定不是答案 所以mid+1跳过mid
                left = mid + 1
            else:
                right = mid # mid对应的值>=target 可能是答案 所以不能跳过mid
        return left
    
'''
variant:You are conducting an A/B test and need to randomly pick a person from a user base spread across multiple cities. 
Each city has a known population, and you need to ensure that the probability of choosing a user from each city is proportional 
to the city's population.
You are given a 0-indexed array of pairs city_populations , where each pair consists of a string representing the name of 
the ith city, and an integer representing the population of the ith city 
(in millions, but treat these values as if in ones for computation purposes).
You need to implement the function pickIndex(),which randomly picks a person and returns the name of the city the person is in.

Example 1:
Input['Solution" ,"pickIndex" ,"pickIndex"]
[[['seattle",500], ['New York",900], ["Los Angeles",400],[],[]]
Output: [null,"New York", "Los Angeles"]
思路:同OG.
'''
class RandomPickPerson:
    def __init__(self, items: List[tuple[str, int]]):
        self.items = items
        self.prefix_sum = [0] * len(items)
        self.prefix_sum[0] = items[0][1]
        for i in range(1, len(items)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + items[i][1]
    def pick_city(self, person:Optional[int]=None) -> int: # person参数方便testing
        target = random.randint(1, self.prefix_sum[-1]) if not person else person # 随机一个[1, max_prefix_sum]之间的整数
        # 二分找第一个大于等于target的前缀和的值 并返回对应的下标
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target: # mid对应的值比target小 一定不是答案 所以mid+1跳过mid
                left = mid + 1
            else:
                right = mid # mid对应的值>=target 可能是答案 所以不能跳过mid
        return self.items[right][0]

# test
items = [('seattle', 500), ('New York', 900), ('LA', 400)]
items = [('US', 300), ('VN', 100), ('BR', 200)]
obj = RandomPickPerson(items)
print(obj.pick_city(125)) # US
print(obj.pick_city(299)) # US
print(obj.pick_city(300)) # US
print(obj.pick_city(305)) # VN
print(obj.pick_city(399)) # VN
print(obj.pick_city(600)) # BR