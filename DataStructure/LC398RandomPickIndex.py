from typing import List
import collections, random

class Solution:
    def __init__(self, nums: List[int]):
        self.dict = collections.defaultdict(list) # dict: {val: [idex0, idx1, ...]}
        for i in range(len(nums)):
            self.dict[nums[i]].append(i)      

    def pick(self, target: int) -> int:
        indexList = self.dict[target]
        return random.choice(indexList) # Return a random element from the non-empty indexList. If indexList is empty, raises IndexError.

# followup: O(1) space. 
'''
思路:reservoir sampling
遍历数组 在遍历过程中 只关注值为target的元素
设已经看到的第count个target值的位置是i
以概率1/count选择当前下标i. 最终返回被选中的下标.
T(n) S(1)
'''
def pick_random_index(nums: List[int], target: int) -> int:
    count = 0
    res = -1
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
            # 以1/count的概率选当前下标
            if random.randint(1, count) == 1:
                res = i
    return res

'''注意下面的约束条件 主动问 可能不会直接给出
variant1: Given an integer array nums of possible duplicates, 
randomly output k numbers and return them as an integer array. 

条件1:You cannot pick a number twice or replace an existing picked number
with an already picked number in the resulting integer array.

条件2:Note that you must do this without using extra space complexity.
Furthermore, you must write an algorithm with 0(n) runtime complexity.
思路:reservoir sampling
1.初始化:将前k个元素作为候选结果 即“蓄水池”
2.对于第i(i ≥ k)个元素:
以k/i的概率将其加入蓄水池 随机替换池中一个元素
最终每个元素进入最终结果的概率均为k/n  n是总元素数
'''
def sample_k(nums: list[int], k:int) -> list[int]:
    ret = nums[:k]
    for i in range(k, len(nums)):
        n = i + 1
        idx = random.randrange(n) # 随机返回一个[0,n-1]的整数
        if idx < k: # 可以替换ret内的某个元素
            ret[idx] = nums[i]
    return ret

'''
variant2: What if you had to use reservoir sampling to pick an index of the maximum value in the array?
思路:遍历数组元素 当前值nums[i]等于最大值 → 进行蓄水池采样
在遇到第count个最大值时 以1/count的概率保留这个索引 替换之前的picked_index
举例:
第1个最大值:一定被选中 cnt更新为1, 第2个最大值:有1/2的概率替换第一个
第n个最大值:有1/n的概率被选中.这样可以保证每个最大值元素被选中的概率相同.
T(n) S(1)
'''
def sample_max_index(nums:list[int]) -> int:
    max_num = float('-inf')
    cnt = 0
    picked_idx = -1
    for i in range(len(nums)):
        if nums[i] < max_num:
            continue
        elif nums[i] > max_num:
            cnt = 1
            picked_idx = i
            max_num = nums[i]
        else: # nums[i] == max_num
            cnt += 1
            if random.randrange(cnt) == 0:
                picked_idx = i
    return picked_idx