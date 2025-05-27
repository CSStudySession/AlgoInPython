# 双指针. sort数组后 对i: left --> xxxx <--right. 
# T(n^2) S(n)from python sort
def threeSumClosest(nums: list[int], target: int) -> int:
    diff = float("inf")
    nums.sort()
    ret = 0
    for i in range(len(nums)):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - sum) < diff:
                diff = abs(target - sum) # 注意取abs
                ret = sum # 注意更新ret
                if diff == 0: # 可以提前break
                    break
            if sum < target:
                lo += 1
            else:
                hi -= 1
    return ret

'''
variant:two sum closest. return the difference between the sum of the two integers and the target.
Two Pointers: 先将数组排序 使用两个指针start和end从两端向中间移动
计算两个数的和与目标值target的差值 记录最小差值. 根据当前和与目标的大小关系调整指针位置
遇到正好相等的情况直接返回差值0. 最后返回最小差值
T(nlogn) S(n) if count for sort(), otherwise S(1)
'''
def two_sum_closest(nums, target):
    # 初始设定最小差值为一个较大值
    min_diff = float('inf')
    # 如果数组为空或长度小于2，则直接返回
    if not nums or len(nums) < 2:
        return min_diff
    nums.sort()
    start = 0
    end = len(nums) - 1
    # 双指针查找最接近目标值的两个数之和
    while start < end:
        total = nums[start] + nums[end]
        min_diff = min(min_diff, abs(target - total))
        if total < target:
            start += 1
        elif total > target:
            end -= 1
        else:  # 如果刚好等于 target，就返回0
            return 0
    return min_diff