from typing import List
# two pointer + sliding window. l,r分别是窗口的左右端点
# 1.先用right遍历 遇到0就cnt+1 先找到第一个window
# 2.更新window: cnt>k时, 看left, 如果左端点是0, cnt-1.然后left+1
def longestOnes(nums: List[int], k: int) -> int:
    left, right = 0, 0
    maxLen = 0
    cnt = 0
    while right < len(nums):
        if nums[right] == 0: #cnt目前找到了几个0(可以作为1)
            cnt += 1
        # 找到了一个window 需要更新window
        while cnt > k:
            if nums[left] == 0:
                cnt -= 1
            left += 1
        maxLen = max(maxLen, right - left + 1)
        right += 1
    return maxLen

# variant. 
# 1. given a char array with 'H'(holidays) and 'W'(workdays), or 
# 2. given a bool array with True and False.
# return max of concective holidays with given PTO (in int).
# 思路完全一样 two pointer forming a sliding window
def longestHolidays(days: List[str], k: int) -> int:
    if not days:
        return 0
    max_vacation = 0
    left, right = 0, 0
    while right < len(days):
        if days[right] == 'W':
            pto -= 1
        while pto < 0:
            if days[left] == 'W':
                pto += 1
            left += 1
        max_vacation = max(max_vacation, right - left + 1)
        right += 1
    return max_vacation  
'''
followup
1. Does the performance of code depend on what the input is? 
Like what input would make the code perform most computation. 
ans: "WWWW"(basically all Workdays) and pto=0
2. What happens if you accrue 1 PTO day every week. How would code change? 
ans: add a if condition at beginning of loop
if(right % 7 == 0) pto++
'''