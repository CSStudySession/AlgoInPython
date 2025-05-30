'''
1. 从右往左 找第一个“波峰”位置x: ...<= x >= ... 多个相同x取最靠左的
含义:波峰右边已经是降序 即最大排列 从x-1处动手 才可能改大
2. 记x左边第一个元素为y 从x开始往右找 第一个最远的>y的值z, swap(y,z)
含义:换y才能让数变大(右边已经是降序 即最大) 右边是降序 找最靠右的 才能让整体最小幅度变大  
3. 从x位开始 reverse数组 [x:][::-1]
含义:交换完后 右边部分依旧是降序(最大排列) 希望它是最小排列 所以需要反转成升序 才能得到最小的“下一个排列”
T(n) S(1)
'''
def nextPermutation(nums: list[int]) -> None:
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
    # 反转从end_idx之后的部分
    lo, hi = end_idx, len(nums) - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

''' 
variant1: return previous permutation:第一个比当前值小的
1. 从右往左 找第一个“波谷”位置x: ...>= x <= ... 多个相同x取最靠左的
含义: 波谷右边已经是升序 即最小排列 从x-1处动手 才可能改小
2. 记x左边第一个元素为y 从x开始往右找 最后一个 < y 的值z swap(y, z)
含义: 换 y 才能让数变小（右边是升序，即最小） 找最靠右的 < y 才能让整体最小幅度变小
3. 从x位开始 reverse数组 [x:][::-1]
含义: 交换完后右边部分依旧是升序（最小排列）希望它是最大排列 所以需要反转成降序 才能得到最大的“前一个排列”
'''
def prevPermutation(nums: list[int]) -> None:
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
    # 反转从end_idx之后的部分
    lo, hi = end_idx, len(nums) - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1

# test
nums = [9,4,8,3,5,5,8,9]
prevPermutation(nums)
print(nums)