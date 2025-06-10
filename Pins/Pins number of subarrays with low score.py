'''
给定一个正整数数组 nums 和一个整数 k, 返回得分小于 k 的非空子数组的个数。
子数组定义：数组中连续的一段。
得分定义：子数组的得分 = 子数组的元素和 * 子数组的长度。
输入:nums: List[int]，正整数数组，不能为空
k: int 整数 k ≥ 1
输出:int 满足条件的非空子数组数量
Clarification:
问题	               答案
数组可以为空吗？ 	     否
数组可以有负数或 0 吗？	  否，只有正整数
k可以为无效值吗?	     否 k ≥ 1
score == k 的算不算？	不算，必须 < k
'''

'''
方法1:Sliding Window (最优解)
双指针维护窗口 [left, right]
如果当前窗口得分 ≥ k 则收缩左端点
每次移动right 窗口内的所有子数组都合法
T(n) S(1)
'''
def count_subarrays_sw(nums: list[int], k: int) -> int:
    total = 0  # 当前窗口的元素和
    result = 0
    left = 0
    for right in range(len(nums)):
        val = nums[right]
        total += val
        # 窗口得分 = total * 长度，如果太大，收缩左端点
        while total * (right - left + 1) >= k:
            total -= nums[left]
            left += 1
        # 此时窗口内所有子数组都合法 数量为(right - left + 1)
        result += right - left + 1
    return result

'''
方法2: binary search
对于每一个起点i, 我们希望找到最远的右端点j, 使得子数组 nums[i..j]的score:
sum(nums[i..j]) * len(nums[i..j]) < k. 得分随着右端点j的增加 单调递增(因为都是正数) 
所以可以用二分找最大合法的j.
T(nlogn) n个起点 每个都二分一次  S(n)
'''
def count_subarrays_bs(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    def find_max_right(left: int) -> int:
        lo, hi = left, n - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            left_sum = prefix_sum[left - 1] if left > 0 else 0 
            total = prefix_sum[mid] - left_sum
            length = mid - left + 1
            if total * length >= k: # >=k 右边包括mid 都不可能是答案 跳过右边
                hi = mid - 1
            else:
                lo = mid
        return hi

    result = 0
    for left in range(n):
        if nums[left] >= k:
            continue
        right_most = find_max_right(left)
        result += (right_most - left + 1)
    return result

assert count_subarrays_bs([2, 1, 4, 3, 5], 10) == 6