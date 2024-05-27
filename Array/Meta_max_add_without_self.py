from typing import List
import sys

def max_two_add_without_self(numsA: List[int], numsB: List[int]) -> int:
    if not numsA and not numsB: return 0

    maxA = [-sys.maxsize - 1] * len(numsA)
    maxB = [-sys.maxsize - 1] * len(numsB)
    prev_maxA, prev_maxB = numsA[0], numsB[-1]

    for i in range(1, len(numsA)): 
        maxA[i] = prev_maxA     # 注意这里先给maxA数组赋值 然后再更新pre_maxA: 不能包括当前的nums[i]
        prev_maxA = max(prev_maxA, numsA[i])

    for j in range(len(numsB) - 1, -1, -1): 
        maxB[j] = max(prev_maxB, numsB[j])  # maxB可以包括当前的numsB[i] 所以直接取历史最大的
    
    min_len = min(len(numsA), len(numsB))
    ret = -sys.maxsize - 1
    # 从第二个元素开始看 因为numsA第一个元素永远取不到
    # 如果面试官说第一个元素取不到按照值为0算 就if(k == 0)特判一下 只取maxB[0]
    for k in range(1, min_len):
        ret = max(ret, maxA[k] + maxB[k])
    return ret


# 测的时候 可以把numsA/B换个顺序输入函数 就变成一个长一个短了
numsA = [2, 5, 3]
numsB = [11, 4, 6, 7, 10]
print(max_two_add_without_self(numsA, numsB))
