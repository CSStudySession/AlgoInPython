from typing import List
from typing import Dict
class Solution:
    def subarraySum_v0(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefix_sum = 0
        dict: Dict[int, int] = {}  # {prefix_sum: times}
        dict[0] = 1 #先count1, 当取全部长度的时候容易miss
        cnt = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if (prefix_sum - k) in dict:
                cnt += dict[prefix_sum - k]
        
            if prefix_sum not in dict:
                dict[prefix_sum] = 1
            else:
                dict[prefix_sum] += 1
        return cnt
    
    def subarraySum_v1(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        prefix_sum = [0] * (len(nums) + 1)
        prefix_sum[0] = 0
        # construct prefix_sum: s[i] = s[i-1] + num[i]
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1] 
        # enumerate endpoint
        ret = 0
        prev_dict = {0 : 1} # 前0项和为0 出现过1次
        for i in range(1, len(nums) + 1):
            ret += prev_dict.get(prefix_sum[i] - k, 0)
            prev_dict[prefix_sum[i]] = prev_dict.get(prefix_sum[i], 0) + 1
        return ret