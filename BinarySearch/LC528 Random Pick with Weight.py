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
'''

import random
from typing import List

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

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()