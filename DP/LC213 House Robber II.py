'''
https://leetcode.com/problems/house-robber-ii/?envType=company&envId=apple&favoriteSlug=apple-three-months

状态机dp    
'''
from typing import List

class Solution:
    # 状态机dp
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        size = len(nums)
        # f[i][j] 第i号点 取(j==1)或者不取(j==0)
        dp = [[0,0] for i in range(size + 1)]
        # 枚举第1号点 取或者不取. 它决定了最后一个点是否能取
        # 第1号点取 dp[1][0]这个状态就非法 赋值负无穷
        dp[1][0] = -1e5
        dp[1][1] = nums[0]
        for i in range(2, size + 1):
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
        
        ret = dp[size][0] # 第1号点取了 最后一个点只能不取
        
        # 第1号点不取 dp[1][1]状态非法 赋值负无穷
        dp[1][1] = -1e5
        dp[1][0] = 0  # 注意这里要对dp[1][0]重新赋值 上面的逻辑修改过dp[1][0]
        for i in range(2, size + 1):
            dp[i][1] = dp[i - 1][0] + nums[i - 1]
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
        
        ret = max(ret, dp[size][1], dp[size][0])
        return ret