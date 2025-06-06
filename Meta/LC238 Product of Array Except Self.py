'''
思路:前后缀分解
- 前缀乘积用数组prefix表示prefix[i]:前i-1个数的乘积(不包括第i个数) 容易
得出:prefix[i] = prefix[i-1] * nums[i-1]
- 后缀乘积也可以用数组表示 但是题目要求space O(1)复杂度 所以后缀乘积用一个变量suffix表示 
然后on the flight的从后往前计算答案 先更新prefix[i] 再更新suffix
T(n) S(1)
'''
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    for i in range(1, n): # 先计算前缀乘积数组
        prefix[i] = prefix[i - 1] * nums[i - 1]
    suffix, idx = 1, n - 1 # 从后往前 计算后缀乘积suffix
    while idx >= 0:
        prefix[idx] = prefix[idx] * suffix # in-place update prefix[i] as final result
        suffix *= nums[idx] # 每次更新完答案 也要更新suffix 给下一次计算用
        idx -= 1
    return prefix