'''
https://leetcode.com/problems/product-of-array-except-self/description/?envType=company&envId=apple&favoriteSlug=apple-six-months&status=TO_DO

前后缀分解问题
前缀乘积用数组prefix表示 prefix[i]:前i-1个数的乘积(不包括第i个数) 容易得出:prefix[i] = prefix[i-1]*nums[i-1]
后缀乘积也可以用数组表示 但是题目要求space O(1)复杂度 所以后缀乘积用一个变量suffix表示 然后on the flight的从后往前计算答案 同时更新suffix
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
 
        for i in range(1, n): # 先计算前缀乘积数组
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix, idx = 1, n - 1 # 从后往前
        while idx >= 0:
            prefix[idx] = prefix[idx] * suffix
            suffix *= nums[idx] # 每次更新完答案 也要更新suffix 给下一次计算用
            idx -= 1
        
        return prefix