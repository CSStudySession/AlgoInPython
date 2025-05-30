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
        if nums[mid] > nums[mid + 1]: # ans in [left, mid]
            right = mid
        else:
            left = mid + 1
    return right

'''
variant1: find a vally element. assume:nums[-1] = nums[n] = +inf, no duplicates
T(logn) S(1)
'''
def find_vally_element(nums: List[int]) -> int: # 返回vally item的index
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
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
variant2: find a peak element. assume:nums[-1] = nums[n] = -inf, allow duplicates, and 
peak is defined as a <= peak >= b. (if peak is defined as a < peak > b, code logic still holds.)
当mid和mid+1值相等时 为何right-=1正确?
- mid+1 <= right, mid值和mid+1值相等 所以[left,right-1]至少有一个解. 画折线图可以看出来.
- 所以不管right是不是peak 可能是 但是可以丢掉. 左边还有其他解可以找到.
T(n) S(1)
'''
def find_peak_element_with_dups(nums: List[int]) -> int: # 返回peak item的index
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]: # ans in [left, mid]
            right = mid
        elif nums[mid] < nums[mid + 1]: # ans in [mid+1, r]
            left = mid + 1
        else: # 不能确定左右哪边是答案 右指针移动一位
            right -= 1
    return right

# test
nums = [4,4,2,7,6,6,1]
print(find_peak_element_with_dups(nums))

'''
variant3:find either a Valley or Even Terrain (a triplet being equal). return any one of index.
要点:数组允许重复元素 寻找一个valley或者三个等长的位置.
还是二分. 注意valley的定义会影响得到mid后的特判逻辑. 如果是严格小于两边, 平地和valley要分开检查.
T(n) S(1) worst case linear scan
'''
def find_valley_or_even_terrain(nums: List[int]) -> int:
    size = len(nums)
    if size <= 1:
        return 0

    left, right = 0, size - 1

    while left < right:
        mid = (left + right) // 2

        left_val = nums[mid - 1] if mid > 0 else float('inf')
        right_val = nums[mid + 1]

        # 检查 valley or 平地
        if nums[mid] <= left_val and nums[mid] <= right_val:
            return mid

        # 决定搜索方向
        if nums[mid] > nums[mid + 1]: # 解在[mid+1,r]区间
            left = mid + 1
        elif nums[mid] < nums[mid + 1]:
            right = mid
        else:
            right -= 1  # 相等，不能确定趋势，收缩右边界
    return right  # 最终收敛