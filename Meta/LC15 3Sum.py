
# 解法1 Two Pointers 找到所有a+b = -c的unique pair. input may have duplicate->output unique
# T O(n^2) time  S(n) -> from python sorted()
def threeSum(self, nums: list[int]) -> list[list[int]]:
    if not nums: return []
    ret = []
    nums = sorted(nums)
    for i in range(len(nums)):
        # skip duplicate triples with the same first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        left, right = i + 1, len(nums) - 1 # 不回头 只需要[i+1, right]这一段
        self.findTwoSumPair(left, right, nums, target, ret)    
    return ret

def findTwoSumPair(self, left, right, nums, target, ret):
    triple = []
    while left < right:
        if nums[left] + nums[right] == target:
            triple = [nums[left], nums[right], -target]
            ret.append(triple) # update final results
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:#此时要left-1, 因为left已经前进了一个 需要和前面的比较
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1