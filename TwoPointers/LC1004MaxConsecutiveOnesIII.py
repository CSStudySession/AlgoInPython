from typing import List

class Solution:
    # two pointer + sliding window. l,r分别是窗口的左右端点
    # 1.先用right遍历 遇到0就cnt+1 先找到第一个window
    # 2.更新window: cnt>k时, 看left, 如果左端点是0, cnt-1.然后left+1
    
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLen = 0
        cnt = 0
        
        for right in range(len(nums)):
            if nums[right] == 0: #cnt目前找到了几个0(可以作为1)
                cnt += 1
            
            # 找到了一个window 需要更新window
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen