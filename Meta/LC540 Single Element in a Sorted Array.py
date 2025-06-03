'''
有序数组 只有1个数仅出现1次 其他都出现两次 找到这个数.
每一对重复数字在数组中必然是成对出现的 并且位置为[even, even+1] 利用这个性质:
二分下标 mid
如果mid是odd -> mid -= 1转化成even
如果中点mid是even 且nums[mid] == nums[mid+1] 说明单个元素在右边
如果中点mid是偶数 且nums[mid] != nums[mid+1] 说明单个元素在左边 可能包括mid
通过移动 left 和 right 最终会定位在这个唯一的数上
T(logn) S(1)
'''
def singleNonDuplicate(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1: # odd idx转成even
            mid -= 1  # odd最小从1开始 所以一定不会越界 
        if nums[mid] != nums[mid + 1]:
            right = mid  # mid可能是答案 所以不能扔掉
        else:
            left = mid + 2 # 跳过当前重复的pair
    return nums[right]