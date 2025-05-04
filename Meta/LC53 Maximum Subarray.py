'''
思路: 当前的最大子数组和 = prefix_sum - 之前最小的prefix_sum
最小前缀和min_sum就像“之前最差的历史” 我们找从那里到现在的“反弹最大值”
'''
def maxSubArray(nums: list[int]) -> int:
    if not nums:
        return 0
    prefix_sum, min_sum = 0, 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        prefix_sum += nums[i]
        max_sum = max(max_sum, prefix_sum - min_sum)
        min_sum = min(min_sum, prefix_sum) # 注意先更新max 后更新min
    return max_sum