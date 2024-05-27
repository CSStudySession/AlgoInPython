from typing import List 
import sys
'''
给定一个nums数组 返回数组中两个元素的最大和. 要求这两个元素不能相邻.

思路:
扫描数组nums, 记当前index为i. 维护一个i-1之前的看到过的最大数 记为tmp_max. 
tmp_max和当前的nums[i]求和作为备选答案 与维护的global ret进行对比.
'''

def max_sum_of_two(nums: List[int]) -> int:
    if not nums or len(nums) < 3: return 0   # nums至少有三个数

    tmp_max = max(nums[0], nums[1])
    ret = nums[0] + nums[2]
    for i in range(3, len(nums)):             # 从第四个数开始看
        tmp_ret = tmp_max + nums[i]
        ret = max(ret, tmp_ret)
        tmp_max = max(tmp_max, nums[i - 1])
    return ret

nums = [4, 5, 102, 2]
# nums = [1, 2, 3, 4, 5]
print(max_sum_of_two(nums))