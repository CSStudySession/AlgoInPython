from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2: 
            return
        
        end_idx = len(nums) - 1
        while (end_idx and nums[end_idx - 1] >= nums[end_idx]):
            end_idx -= 1
        if end_idx <= 0:
            nums.reverse()
            return
        # 在[end_idx, end]中 找比nums[end_idx-1]大的 第一个最远的位置
        idx = end_idx
        while idx < len(nums) and nums[idx] > nums[end_idx - 1]:
            idx += 1
        nums[end_idx - 1], nums[idx - 1] = nums[idx - 1], nums[end_idx - 1]
        nums[end_idx:] = nums[end_idx:][::-1]