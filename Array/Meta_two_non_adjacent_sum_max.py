import heapq
'''
给定一个nums数组 返回数组中两个元素的最大和. 要求这两个元素不能相邻.
解法1:
扫描数组nums, 记当前index为i. 维护一个i-1之前的看到过的最大数 记为tmp_max. 
tmp_max和当前的nums[i]求和作为备选答案 与维护的global ret进行对比.
'''

def max_sum_of_two(nums: list[int]) -> int:
    if not nums or len(nums) < 3: return 0   # nums至少有三个数

    tmp_max = max(nums[0], nums[1])
    ret = nums[0] + nums[2]
    for i in range(3, len(nums)):             # 从第四个数开始看
        tmp_ret = tmp_max + nums[i]
        ret = max(ret, tmp_ret)
        tmp_max = max(tmp_max, nums[i - 1])
    return ret

nums = [4, 5, 102, 2]
# nums = [1, 2, 3, 4, 5]
# print(max_sum_of_two(nums))

'''
解法2: 维护一个最小堆 最多只保留数组中最大的4个元素及其下标
遍历堆中两个数的组合 找下标满足相差>=2的最大组合
T(n) S(1)
'''
def maxSumOfNonAdjacentPair(A):
    # 维护一个最小堆，最多只保留数组中最大的4个元素及其下标
    top4 = []
    for i, v in enumerate(A):
        heapq.heappush(top4, (v, i))
        if len(top4) > 4:
            heapq.heappop(top4)
    # 转换为列表，避免堆结构带来排序干扰
    top_elements = list(top4)
    # 计算满足下标差至少为2的最大值组合
    max_sum = float('-inf')
    for i in range(len(top_elements)):
        for j in range(i + 1, len(top_elements)):
            val1, idx1 = top_elements[i]
            val2, idx2 = top_elements[j]
            if abs(idx1 - idx2) >= 2:
                max_sum = max(max_sum, val1 + val2)
    return max_sum

A = [1, 5, 3, 8, 12, 2]
print(maxSumOfNonAdjacentPair(A))