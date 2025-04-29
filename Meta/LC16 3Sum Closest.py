
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