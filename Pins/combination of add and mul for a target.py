'''
Given a list and a target number, return true if any combination of addition and/or multiplication of the list numbers hits the target
Notes:

You can ignore order of operations
Numbers must be used left to right and cannot reorder numbers in the list
Ex.
list = [2,3,5], target = 25 -> true, because 2 + 3 * 5 = 25
list = [2,3,5], target = 12 -> false, because no way to get 12

'''

from typing import List

# option 1: recursive
def can_hit_target(nums:List[int], target:int) -> bool:
    if not nums:
        return False 
    return conbination_operations(nums, target, 1, nums[0]) # 注意递归下标从1开始 nums[0]当成初始值传入了

def conbination_operations(nums:List[int], target:int, index:int, cur_val:int) -> bool:
    if target == cur_val:
       return True
    
    if index >= len(nums) or cur_val > target:
       return False
    
    return conbination_operations(nums, target, index + 1, cur_val + nums[index]) or conbination_operations(nums, target, index + 1, cur_val * nums[index])
    
# option 2: iterative
def can_hit_target_iter(nums:List[int], target:int) -> bool:
    if len(nums) == 0:
        return False

    stack = [(nums[0], target, 0)]   # tuple三元组的意义: 当前计算结果, 目标值, 数组元素下标

    while(stack):
        elem, ret, idx = stack.pop()
        if elem == target and idx == len(nums) - 1:
            return True
        if idx + 1 < len(nums):
            # 分别计算 加/乘 下一个元素
            add, mul = elem + nums[idx + 1], elem * nums[idx + 1]
            # 分别计算 加/乘 之后还剩下多少需要凑出来
            add_ret, mul_ret = ret - add, ret - mul
            # 两个tuple都扔stack上
            stack.append([add, add_ret, idx + 1])
            stack.append([mul, mul_ret, idx + 1])
        
    return False   # 凑不出来 return False

# Example usage
nums1 = [2, 3, 5]
nums2 = [4]
nums3 = [1, 2, 3, 5]
target1 = 25
target2 = 5
target3 = 7

print(can_hit_target(nums1, target1))
print(can_hit_target(nums2, target2))
print(can_hit_target(nums3, target3))

print(can_hit_target_iter(nums1, target1))
print(can_hit_target_iter(nums2, target2))
print(can_hit_target_iter(nums3, target3))