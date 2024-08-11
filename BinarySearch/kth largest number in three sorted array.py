'''
给定三个排好序的数组, 求三个数组的数都考虑进去后的第k大的数。要求log(n)的时间复杂度

思路:
对于每个数组，我们可以计算出有多少个元素小于等于一个给定的值。如果将所有三个数组的计算结果加起来，
看看是否有恰好 k 个元素小于等于这个给定的值，那么我们就找到了第 k 大的数。这个方法利用了二分查找的特性，
可以在 O(log(n)) 的时间复杂度内完成。
'''
from typing import List

def count_less_equal(nums:List[int], target:int) -> int:
    """Return the count of elements less than or equal to target in nums."""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left + 1 # 返回元素个数 所以要+1 (left是下标)

def kth_largest_in_three_sorted_arrays(arr1:List[int], arr2:List[int], arr3:List[int], k:int) -> int:
    """Find the k-th largest element considering all three sorted arrays."""
    left, right = min(arr1[0], arr2[0], arr3[0]), max(arr1[-1], arr2[-1], arr3[-1])
    
    while left < right:
        mid = (left + right) // 2
        # count_less_equal
        count = count_less_equal(arr1, mid) + count_less_equal(arr2, mid) + count_less_equal(arr3, mid)

        if count < k:        # mid一定不是答案 答案在[mid+1, right]之间找
            left = mid + 1
        else:                # mid可能是答案
            right = mid
    
    return left

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = [0, 9, 10, 11]
k = 5

print(kth_largest_in_three_sorted_arrays(arr1, arr2, arr3, k))  # Output should be the 5th largest number


