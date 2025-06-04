'''注意: 数组元素不重复！
使用标准二分查找，但在每一步判断时，识别哪一部分是有序的，然后判断 target 是否落在该有序区间中。
步骤：
取 mid = (left + right) // 2  如果 nums[mid] == target 直接返回
- 如果左半边 [left, mid] 是升序的：
判断 target 是否在 [left, mid) 之间，如果是，就收缩 right
否则在右半边，收缩 left
- 否则右半边 [mid, right] 是升序：
判断 target 是否在 (mid, right] 之间，若是，收缩 left
否则收缩 right
T(logn) S(1)
'''
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right: # 这个模板 是<= 二分结束时 left > right
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # 左半边有序
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # 目标在左边
            else:
                left = mid + 1   # 目标在右边
        # 右半边有序
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # 目标在右边
            else:
                right = mid - 1  # 目标在左边
    return -1 # 找不到 返回-1

'''
followup: 数组元素有重复. leetcode 81 search rotated sorted array II
二分查找：初始化 left = 0, right = len(nums)-1 每次取 mid = (left + right) // 2。
若找到目标，立即返回 True。
遇到重复元素时特殊处理：
当 nums[left] == nums[mid]时 无法判断是左半边有序还是右半边有序（因为中间可能全是重复的）
这时执行left += 1 跳过重复元素 保证能收缩区间
判断哪一边是有序的：
- 如果 nums[left] <= nums[mid] 说明左半部分是升序的
若target在左半区间范围内 nums[left] <= target < nums[mid] 则在左边找 right = mid - 1。
否则在右边找 left = mid + 1。
- 否则右半部分是升序的
若target在右半区间 nums[mid] < target <= nums[right] 则在右边找 left = mid + 1。
否则在左边找 right = mid - 1。
如果不能在二分过程中返回 最后返回false
T(n) 最差情况是linear search 数组元素都一样  S(1)
'''
def search(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[left]: # 不能判断哪边有序 先收缩边界
            left += 1
            continue
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False