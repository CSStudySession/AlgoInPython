'''
N robots on a line. Find a point such that the total distance traveled by all robots is minimized.

Input:
The position pi of each robot i={1, 2, ..., N}, unsorted array
Output:
meeting point x* such that the total distance traveled by all individuals is minimized.

x* = min_x: sum(|x - p_i|) -> convex function because sum of convex funtions is also convex.
形象得想 在数轴上 如果起初把meeting point定在median 然后再把meeting point往左或者右移动delta 可以发现 距离之和
一定会增加delta. 所以median是最优meeting point
'''

from typing import List

def find_median(nums: List[float]) -> float:
    if not nums:
        return 0.0
    target_th = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
    idx = partition(nums, target_th, 0, len(nums) - 1)
    return nums[idx]

def partition(nums:List[float], k:int, start:int, end:int) -> int:
    if start >= end:                                # corner case: keys is empty. start = 0, end = -1
        return start
    
    left, right = start - 1, end + 1    # 每次用start的后一个 和end的前一个相比 (含义是[start, left], [right, end]已经排好序了)
    pivot = nums[(left + right) // 2]   # pivot选择中间点的值 比较保险 
    while left < right:
        while True:
            left += 1
            if nums[left] >= pivot:    # left从左往右找第一个>=pivot的数
                break
        while True:
            right -= 1                 # right从右往左找第一个<=pivot的数
            if nums[right] <= pivot:
                break
        if left < right:               # 交换l,r指向的数 注意这里l,r交换后 不会加一/减一
            nums[left], nums[right] = nums[right], nums[left]
    
    if k <= right - start + 1:        # 左边区间[s, r]有(r-s+1)个数字 k<=它 说明第k小的数 落在[s,r]内 往左递归
        return partition(nums, k, start, right)
    else:                             # 在右边区间里 找第 k-(r-s+1)小的数字 左半边区间已经有(r-s+1)个数字了 所以要减掉
        return partition(nums, k - (right - start + 1), right + 1, end)

# nums = [4.1, 2.2, 2.4, 1.8, 5.4, 6.9]
nums = [4.1, 2.2, 2.4, 1.8, 5.4]
print(find_median(nums))

'''
followup: 如果数组太大 无法放到一台机器上 如何分布式求解?
利用p-persentile distributed calcuation求解

步骤 1:数据分割
将大数组分割成若干小块，每块数据可以放入单台机器进行处理。假设有 N 台机器，那么将数组分割成 N 块，每块由一个机器负责处理。

步骤 2: 初始候选选择
随机选择一些数据点作为候选中位数。这些候选点可以从数据块中随机采样得到。

步骤 3: 分布式统计
将这些候选中位数广播到所有机器上，并在每个机器上计算其数据中小于等于每个候选的个数。

步骤 4: 汇总统计结果 
协调节点汇总所有机器上的统计结果，计算全局范围内每个候选的累计个数。

步骤 5: 调整搜索范围
根据累计个数和目标中位数的位置，调整候选的搜索范围。重复步骤 2 到 4, 直到搜索范围收敛。
'''
'''
import random
import numpy as np

# 将数据分割成若干块
def split_data(data, num_chunks):
    return np.array_split(data, num_chunks)

# 生成初始候选中位数
def initial_candidates(data_chunks, num_candidates):
    all_data = np.concatenate(data_chunks)
    return random.sample(list(all_data), num_candidates)

# 在每个机器上计算小于等于候选的个数
def count_less_equal(data_chunk, candidates):
    return [np.sum(data_chunk <= candidate) for candidate in candidates]

# 汇总所有机器的统计结果
def aggregate_counts(counts_per_machine):
    return np.sum(counts_per_machine, axis=0)

def find_median_distributed(data, num_machines, num_candidates):
    # 将数据分成若干块
    data_chunks = split_data(data, num_machines)
    
    # 初始候选中位数
    candidates = initial_candidates(data_chunks, num_candidates)
    
    # 目标中位数的位置
    median_position = len(data) // 2
    
    while True:
        # 在每个机器上计算小于等于候选的个数
        counts_per_machine = [count_less_equal(chunk, candidates) for chunk in data_chunks]
        
        # 汇总所有机器的统计结果
        total_counts = aggregate_counts(counts_per_machine)
        
        # 找到累计个数刚好超过中位数位置的候选
        for i, count in enumerate(total_counts):
            if count >= median_position:
                current_median = candidates[i]
                break
        
        # 检查是否满足中位数条件
        if total_counts[i] == median_position:
            return current_median
        
        # 更新候选范围
        if total_counts[i] < median_position:
            lower_bound = candidates[i]
        else:
            upper_bound = candidates[i]
        
        # 生成新的候选
        candidates = [random.uniform(lower_bound, upper_bound) for _ in range(num_candidates)]

# 示例数据
data = np.random.randint(0, 100, size=1000)
num_machines = 10
num_candidates = 5

# 求解中位数
median = find_median_distributed(data, num_machines, num_candidates)
print("Estimated median is:", median)
'''