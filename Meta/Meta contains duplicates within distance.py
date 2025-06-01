'''
Given an array of ints, and a postive int k, tell if array has:
array[i] == array[j] and |j - i| <= k
思路:使用dict(val_idx)记录每个元素上一次出现的下标 如果某个元素再次出现 并且当前下标与上一次下标之差不超过k
说明在距离不超过k的范围内存在重复元素 返回True 遍历完后若未找到符合条件的重复项 返回False
T(n) S(n)
'''
def check_duplicates_within_k(nums, k) -> bool:
    val_idx = {}
    for i in range(len(nums)):
        if nums[i] in val_idx:
            if i - val_idx[nums[i]] <= k:
                return True
        val_idx[nums[i]] = i
    return False

# a little better on space. worst case is same.
# 用set记录见过的值 set的大小始终为k-1 每次遍历一个新元素i 先把i-k-1的值从set中删掉
# 再判断当前元素是否在set中 在的话说明距离<=k出现过相同的 返回True 
# T(n) S(k)
def check_duplicates_within_k(nums, k) -> bool:
    val_set = set()
    for i in range(len(nums)):
        if i > k:
            val_set.discard(nums[i-k-1])
        if nums[i] in val_set:
            return True 
        val_set.add(nums[i])
    return False

# test
nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
print(check_duplicates_within_k(nums, k))