# 标准二分
def searchRange(nums: list[int], target: int) -> list[int]:
    if not nums:
        return [-1, -1]
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left  = mid + 1
    if nums[left] != target:
        return [-1, -1]
    left_idx = left
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return [left_idx, right]

# variant1: return the count of a given number
# mostly same as original solution above, but return (right - left_idx + 1)

# variant2: return unique number in array
def count_unique_elements(nums: list[int]) -> int:
    if not nums:
        return 0
    cur, cnt = 0, 0
    while cur < len(nums):
        left, right = cur, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= nums[cur]:
                left = mid
            else:
                right = mid - 1
        cnt += 1 # nums中至少有一个元素 所以一定有解 不需要特判
        cur = right + 1 # 跳过当前所有重复元素 指向下一个不同元素
    return cnt

# test
nums = [1,1,2,2,2,5,5,5,5,6] # 4
# nums = [1,1,1] # 1
# nums = [] # 0
# nums = [5,7,7,9,10,10] # 4
print(count_unique_elements(nums))