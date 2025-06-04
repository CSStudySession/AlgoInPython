from typing import List
'''
要求向右rorate or shift. 三步翻转:
1. 整体翻转 2. 前k个翻转  2. 后n-k个翻转  写一个reverse helper 传入指针即可

如果要求向左rotate? 也是三步翻转 顺序变一下:
1. 翻转前k个  2. 翻转后n-k个  3. 整体翻转
T(n) S(1)
'''
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