'''
给一个数组nums 求能否给数组分成k份 每份不能是空 且每份的和相同. 注意切分不一定是连续的 可以理解为 给原数组分成k组

思路: combination sum类的backtracking
'''
from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:            # k无法整除total 无论如何怎么分都不行
            return False

        target = total // k      # 每份的和记为target 
        used = [False] * len(nums)   # 每个数是否用过 给dfs用

        return self.backtrack(nums, 0, k, 0, target, used)

    def backtrack(self, nums:List[int], start:int, remains:int, current_sum:int, target:int, used:List[bool]) -> bool:
        if remains == 0:  # 所有k份子集都以找完
            return True

        if current_sum == target: # 当前子集凑到了和为target 可以开始下一个子集的拼凑 
            return self.backtrack(nums, 0, remains - 1, 0, target, used)

        for i in range(start, len(nums)):
            if used[i] or current_sum + nums[i] > target: # 当前数字被之前的dfs用过 or 总和>target 跳过当前数字
                continue

            used[i] = True   # 标记当前值被占用 开始dfs
            if self.backtrack(nums, i + 1, remains, current_sum + nums[i], target, used):
                used[i] = False # 回溯回来清理现场
                return True  # dfs的路径上找到了解 不用再循环了 直接返回
            used[i] = False  # dfs路径上没找到解 回溯时清理现场

            '''
            line 40: 在当前递归层级的尝试中 所有可能的数字都不适合作为当前子集的开始数字: 即没有任何数字可以单独成为一个子集的一部分
            '''
            if current_sum == 0: # 这里写成 if start == 0: 也对
                return False
        return False   #尝试了所有可能 都不能成功