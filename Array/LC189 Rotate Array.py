from typing import List

class Solution:
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # 对n取module: 有可能k > n
        
        # 三步翻转法: 整体翻转 前k个翻转 后n-k个翻转
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)