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

# variant1. 输入的pto是int 不是float 下面variant 2可以有decimal
# 1. given a char array with 'H'(holidays) and 'W'(workdays), or 
# 2. given a bool array with True and False.
# return max of concective holidays with given PTO (in int).
# 思路完全一样 two pointer forming a sliding window
def longestHolidays(days: List[str], pto: int) -> int:
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

'''
variant 2: 
# 1. given a char array with 'H'(holidays) and 'W'(workdays), or 
# 2. given a bool array with True and False.
# return max of concective holidays with given PTO (in decimal).

思路: 与variant 1相似 先把整数部分可能拿到的最大结果算出来 
如果有小数的pto 只可能用在left-1或者right+1是workday的前提下 所以加一个check逻辑
T(n) S(1)
'''
def getMaxVacations(days: List[str], pto: float) -> float:
    max_vacation = 0.0
    whole_pto, partial_pto = int(pto), pto - int(pto)
    left = 0
    for right in range(len(days)):
        if days[right] == 'W':
            whole_pto -= 1
        while whole_pto < 0:
            if days[left] == 'W':
                whole_pto += 1
            left += 1
        extension = 0.0   # ext 只可能发生在窗口前后有一个workday的情况
        if left > 0 and days[left - 1] == 'W' or \
            right < len(days) - 1 and days[right + 1] == 'W':
            extension = partial_pto
        max_vacation = max(max_vacation, right - left + 1 + extension)
    return max_vacation

'''
variant3: What if the input data structure is a 2D matrix, not a 1D list? 输入一个2D的工作表 里面都是'W','H'
思路:与1D一样 思考的时候把2d摊平看成一个长的1D数组 转化成上面的问题.

T(m*n) S(1)
'''
# helper func to shrink left pointer.
def shrink_window(days: List[List[str]], left: List[int]) -> List[int]:
    row, col = left[0], left[1]
    if col == len(days[0]) - 1:
        return [row + 1, 0]
    return [row, col + 1]
# main logic
def getMaxVacations(days: List[List[str]], pto: int) -> int:
    max_vacation = 0
    curr_vacation = 0
    left = [0, 0]
    for row in range(len(days)):
        for col in range(len(days[0])):
            if days[row][col] == 'W':
                pto -= 1
            curr_vacation += 1
            while pto < 0: # 收缩左端点 
                if days[left[0]][left[1]] == 'W':
                    pto += 1
                left = shrink_window(days, left) # 函数返回left下一个在2d矩阵中的点
                curr_vacation -= 1
            max_vacation = max(curr_vacation, max_vacation)
    return max_vacation