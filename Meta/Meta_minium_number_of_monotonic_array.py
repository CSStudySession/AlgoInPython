'''
给定一个整数数组 将其拆分成最少数量的monotonic subarrays 每个子数组必须是严格递增或严格递减的
e.g.
[1, 3, 5, 10] → 一个递增段，答案为 1
[7, 4, 2, 2, 2, 1] → 一个递减段（可能不严格） 但还是算作一个，答案为 1
[5, 3, 1, 5, 6, 7] → 5 3 1 递减, 和 5 6 7 递增, 答案为 2
思路: 核心在于检测趋势变化->什么时候从“上升”变成“下降” 或从“下降”变为“上升”
使用一个变量increasing来记录当前趋势
 - None 表示初始未知趋势
 - True 表示当前是递增趋势
 - False 表示当前是递减趋势
遍历数组:
 - 如果当前元素比前一个大，说明是上升趋势
 - 若之前趋势是下降或未初始化 → 说明新的子数组开始
 - 如果当前元素比前一个小，说明是下降趋势
 - 若之前趋势是上升或未初始化 → 新子数组开始
 - 若相等，则跳过（不算趋势变化）
每次趋势改变时，计数器加一
T(n)  S(1)
'''
def count_monotonic_subarrays(nums: list[int]) -> int:
    if not nums:
        return 0
    increasing = None  # 当前趋势：None / True(上升) / False(下降)
    cnt = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if increasing is None or increasing is False:
                increasing = True
                cnt += 1
        elif nums[i] < nums[i - 1]:
            if increasing is None or increasing is True:
                increasing = False
                cnt += 1
        # 若相等，则忽略，保持当前趋势
    return cnt

nums = [1, 3, 5, 10]
# nums = [5, 3, 1, 5, 6, 7]
print(count_monotonic_subarrays(nums))