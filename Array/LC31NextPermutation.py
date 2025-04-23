from typing import List

# 1. 从右往左 找第一个“波峰”位置x: ...<= x >= ... 多个相同x取最靠左的
# 2. 记x左边第一个元素为y 从x开始往右找 第一个最远的>y的值z, swap(y,z)
# 3. 从x位开始 reverse数组 [x:][::-1]
def nextPermutation(nums: List[int]) -> None:
    if len(nums) < 2: 
        return
    end_idx = len(nums) - 1
    while (end_idx and nums[end_idx - 1] >= nums[end_idx]):
        end_idx -= 1
    if end_idx == 0: # end_idx最多在0时 在while条件中就停了 不会越界
        nums.reverse()
        return
    # 在[end_idx, end]中 找比nums[end_idx-1]大的 最远的位置
    idx = end_idx
    while idx < len(nums) and nums[idx] > nums[end_idx - 1]:
        idx += 1
    # 注意swap时 idx要-1 idx最后可能停在越界或者不满足要求的位置
    nums[end_idx - 1], nums[idx - 1] = nums[idx - 1], nums[end_idx - 1]
    nums[end_idx:] = nums[end_idx:][::-1]

# variant1: return revious permutation:第一个比当前值小的
def prevPermutation(nums: List[int]) -> None:
    if len(nums) < 2:
        return 
    end_idx = len(nums) - 1
    while end_idx and nums[end_idx - 1] <= nums[end_idx]: # 注意<= 尽量往左走
        end_idx -= 1
    if end_idx == 0:
        return nums.reverse()
    
    idx = end_idx
    while idx < len(nums) and nums[idx] < nums[end_idx - 1]:
        idx += 1
    nums[end_idx - 1], nums[idx - 1] = nums[idx - 1], nums[end_idx - 1]
    nums[end_idx:] = nums[end_idx:][::-1] # reverse from end_idx

nums = [9,4,8,3,5,5,8,9]
prevPermutation(nums)
print(nums)