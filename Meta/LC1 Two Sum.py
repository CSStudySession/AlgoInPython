from typing import List, collections
# Meta variant 1: return True or False
def has_two_sum(nums: List[int], target) -> bool:
    if not nums:
        return False
    seen_set = set()
    for num in nums:
        other = target - num
        if other in seen_set:
            return True
        seen_set.add(num)
    return False

# Meta variant 2. Given list of pairs[[x1, x2], ...] and a target, 
# return number of unique pairs [a1, a2] and [b1, b2] where a1+b1=target and a2+b2=target
# numbers are limited to digits 0-9. same pair can't be used with itself.
# 思路:linear scan + dict. dict记录扫描过的pair出现的次数.每次用当前pair去检查dict里是否有加起来等于target的pairs
def unique_pairs(pairs: List[List[int]], target: int) -> int:
    if not pairs:
        return 0
    pair_to_freq = collections.defaultdict(int)
    ret = 0
    for pair in pairs:
        first, second = target - pair[0], target - pair[1]
        if (first, second) in pair_to_freq:
            ret += pair_to_freq[(first, second)]
        pair_to_freq[(pair[0], pair[1])] += 1 # 注意这里用pair而非(first,second)更新dict
    return ret
# test
pairs = [[3,4], [1,9], [3,4], [2,1],[9,1], [9,1], [7,6], [1,9]]
target = 10
print(unique_pairs(pairs, target))

# leetcode version. 
def twoSum(nums: List[int], target: int) -> List[int]:
    if not nums: return [-1, -1]
    dict = {} # 存num和对应的下标
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return [i, dict[target - nums[i]]]