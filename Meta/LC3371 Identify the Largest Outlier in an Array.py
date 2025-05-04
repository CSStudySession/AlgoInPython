import collections
'''
思路: 遍历+dict统计数出现的次数
1. 遍历每一个数num 假设它是sum_element
  -- 那么potential_outlier = total_sum - 2 * num
2.check potential_outlier是否在数组中
  -- 与num值相同时 num出现的次数>1 可以当成备选答案
  -- 与num值不同 直接可以当成备选答案
  -- 与ret比较 求max()
T(n) S(n)
'''
def getLargestOutlier(nums: list[int]) -> int:
    tot_sum = sum(nums)
    val_to_cnt = collections.defaultdict(int)
    for num in nums:
        val_to_cnt[num] += 1 # 统计频率
    
    ret = float('-inf')
    for num in val_to_cnt.keys():
        cur = tot_sum - 2 * num
        if cur in val_to_cnt: # 要判断cur是否在原数组中
            if cur != num or val_to_cnt[cur] > 1: # cur与num相等时 对应cnt>1 说明在原数组中是两个数
                ret = max(ret, cur)
    return ret