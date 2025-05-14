import collections
'''
思路:prefix sum + dict: {prefix sum:出现次数}
1.用一个变量prefix_sum来记录从数组开始到当前位置的累加和
2.用一个dict sum_to_cnt来记录每个前缀和出现的次数.
  -- 初始sum_to_cnt[0]=1是为了处理子数组本身就等于k的情况
3.遍历数组时 更新prefix_sum 然后检查prefix_sum-k是否存在于dict中
  -- 若存在 说明在当前位置之前存在某个前缀和 使得从它之后到当前位置的子数组和为k 取对应次数累加
4.更新当前的prefix_sum在dict中的计数
T(n) S(n)
'''
def subarraySum_v0(nums: list[int], k: int) -> int:
    if not nums: return 0
    prefix_sum = 0
    sum_to_cnt = collections.defaultdict(int)  # {prefix_sum: cnt}
    sum_to_cnt[0] = 1 # 前缀和为0 出现过1次. 对应取所有nums的值
    cnt = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if (prefix_sum - k) in sum_to_cnt:
            cnt += sum_to_cnt[prefix_sum - k]
        sum_to_cnt[prefix_sum] += 1
    return cnt

'''
variant1: return true or false.
思路:prefix sum + set {prefix sum}
1.用变量tot来记录从数组开始到当前位置的累加和
2.用一个set prefix_sums来记录出现的每个前缀
  -- 初始set加入0:为了处理子数组本身就等于k的情况
3.遍历数组时 更新tot 然后检查tot-k是否存在于set中
  -- 若存在 说明在当前位置之前存在某个前缀和 使得从它之后到当前位置的子数组和为k 返回true
4.更新当前的tot到set中
T(n) S(n)
'''
def subarraySumExists(nums: list[int], k: int) -> bool:
    tot = 0
    prefix_sums = set([0])
    for num in nums:
        tot += num
        if (tot - k) in prefix_sums:
            return True
        prefix_sums.add(tot)
    return False

'''
variant2: return true or false with given array only contains positive numbers
思路:sliding window. 数组元素都是正数 所以window size只要增大 window里的和一定是单调增的
left,right两个指针 right每前进一次 total+=a[right] 如果tot比k大了 左边窗口收缩.
当tot==k时, 找到合适的窗口. 循环结束 证明找不到该窗口 返回False
T(n) S(1)
'''
def subarray_sum_k_all_positive_item(nums:list[int], k) -> bool:
    left = 0
    tot = 0
    for right in range(len(nums)):
        tot += nums[right]
        while tot > k:
            tot -= nums[left]
            left += 1
        if tot == k:
            return True
    return False