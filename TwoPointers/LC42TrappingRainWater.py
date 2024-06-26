'''
 复杂度
 时间 O(n) 空间(1)
 思路：双指针->相遇问题
 从数组两端走起，每次迭代时判断左pointer和右pointer指向的数字哪个大，
 如果左pointer小，意味着向左移动右pointer不可能使结果变得更好，因为瓶颈在左pointer，
 移动右pointer只会变小，所以这时候我们选择左pointer右移。
 反之，则选择右pointer左移。在这个过程中一直维护最大的那个容积
'''
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        vol = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                ptr = left + 1
                while ptr < right and height[ptr] < height[left]:
                    vol += height[left] - height[ptr]
                    ptr += 1
                left = ptr
            else:
                ptr = right - 1
                while ptr > left and height[ptr] < height[right]:
                    vol += height[right] - height[ptr]
                    ptr -= 1
                right = ptr
        return vol