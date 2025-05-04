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
#print(unique_pairs(pairs, target))

'''
variant: Given an array of positive, sorted, no duplicate integer, and a positive integer k. 
Count of all such subsets of A, such that for any such subset S, Min(S) + Max(S) = k. 
A subset should contain at least two elements. 
for example: 
input: {1,2,3,4,5}. k = 5, then output count = 5 --> {1,4},{2,3},{1,2,4},{1,2,3,4},{1,3,4}

数组有序且无重复 可以利用双指针 从两端查找满足条件的组合
- 使用两个指针 left,right 分别指向数组的开头和结尾
- 若A[left] + A[right] == k:
  -- 在这两个数之间 包含它们 所有的元素都可以用来构成一个合法子集 所以只要枚举 中间元素的所有组合
  -- 只要包含A[left]和A[right] 再从中间任意选0到r-l-1个元素加入 就符合条件
  -- right-left-1个元素 一共可以构成 2^{(right - left - 1)}个不同子集
T(n) S(1)
'''
def count_subsets_with_min_max_sum_k(A, k):
    if not A:
        return 0
    cnt = 0
    left, right = 0, len(A) - 1
    while left < right:
        cur = A[left] + A[right]
        if cur == k:
            window_len = right - left - 1 # 不包含l,r 中间用r-l-1个元素
            cnt += 2 ** window_len  # m个元素的subset个数为2^m 包含空集 
            left += 1
            right -= 1
        elif cur < k:
            left += 1
        else:
            right -= 1
    return cnt

# test
A = [1,2,3,4,5]
k = 5
print(count_subsets_with_min_max_sum_k(A, k))

# leetcode version. 
def twoSum(nums: List[int], target: int) -> List[int]:
    if not nums: return [-1, -1]
    dict = {} # 存num和对应的下标
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            dict[nums[i]] = i
        else:
            return [i, dict[target - nums[i]]]