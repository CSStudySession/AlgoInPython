from typing import List
'''
A peak element is an element that is strictly greater than its neighbors. 
You may imagine that nums[-1] = nums[n] = -∞

followup: 如何提前退出?
在每一轮判断mid是否已经是peak 即比左右都大.如果是 就可以提前退出 而不需要继续收敛到最后一个点. 改动代码如下:
获取左、右的值，注意边界情况
left_val = float('-inf') if mid == 0 else nums[mid - 1]
right_val = float('-inf') if mid == len(nums) - 1 else nums[mid + 1]
# 如果当前是peak 提前退出
if nums[mid] > left_val and nums[mid] > right_val:
    return mid
'''
def findPeakElement(nums: List[int]) -> int: # 返回peak item的index
    if len(nums) == 1:
        return 0
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        left_val = float('-inf') if mid == 0 else nums[mid - 1]
        if left_val < nums[mid] and nums[mid] >  nums[mid] + 1:
            return mid
        if nums[mid] > nums[mid + 1]: # ans in [left, mid]
            right = mid
        else:
            left = mid + 1
    return right

'''
variant1: find a valley element. assume:nums[-1] = nums[n] = +inf, no duplicates
or it may say find local minimum.
T(logn) S(1)
'''
def find_vally_element(nums: List[int]) -> int: # 返回vally item的index
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        left_val = float('inf') if mid == 0 else nums[mid - 1]
        if left_val > nums[mid] and nums[mid] <  nums[mid] + 1:
            return mid
        if nums[mid] > nums[mid + 1]: # ans in [mid+1, r]
            left = mid + 1
        else:
            right = mid
    return right

# test
nums = [1,2,3,1] # 0
nums = [5,2,3,1,6] # 3
# print(find_vally_element(nums))

'''
variant2: find a peak element. assume:nums[-1] = nums[n] = -inf, allow duplicates(nums[i] == nums[i+1])
and peak is defined as a <= peak >= b. (if peak is defined as a < peak > b, code logic still holds.)
思路:由于输入数组允许重复元素 更准确的讲 相邻元素可能相等 所以二分会失效 因为不知道舍弃哪一边 可以用线性扫描做
T(n) S(1)
'''
def find_peak_element_with_dups(nums: List[int]) -> int: # 返回peak item的index
    n = len(nums)
    for i in range(n):
        left = nums[i - 1] if i > 0 else float('-inf')
        right = nums[i + 1] if i < n - 1 else float('-inf')
        if nums[i] > left and nums[i] > right:
            return i
    return -1  # 找不到就返回-1

# test
nums = [4,4,2,7,6,6,1]
#print(find_peak_element_with_dups(nums))

'''
variant3:find either a Valley or Even Terrain (a triplet being equal). return any one of index.
要点:数组允许重复元素(nums[i]可能等于nums[i+1]) 寻找一个valley或者三个等长的位置
由于相邻元素可能相等 无法二分 线性扫描
T(n) S(1)
'''
def find_valley_or_even_terrain(nums):
    n = len(nums)
    for i in range(n):
        left = nums[i - 1] if i > 0 else float('inf')
        right = nums[i + 1] if i < n - 1 else float('inf')
        if nums[i] < left and nums[i] < right:
            return i
        if nums[i] == left and nums[i] == right:
            return i
    return -1  # 找不到就返回-1

arr = [4,5,2,2,4]
print(find_valley_or_even_terrain(arr))