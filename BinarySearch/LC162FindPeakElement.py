from typing import List
'''
A peak element is an element that is strictly greater than its neighbors. 
You may imagine that nums[-1] = nums[n] = -∞
'''
def findPeakElement(nums: List[int]) -> int: # 返回peak item的index
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]: # ans in [left, mid]
            right = mid
        else:
            left = mid + 1
    return right