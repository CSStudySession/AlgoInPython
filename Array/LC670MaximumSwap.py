import collections
# todo: 写注释为什么work
def maximumSwap(num: int) -> int:
    if num < 10: # 只有一位 没得换
        return
    num_str = list(str(num)) #变成str后转成list 方便用下标操作
    for i in range(len(num_str)  - 1):
        if num_str[i] < num_str[i + 1]: # 从前往后找到第一个非递减的位置
            pivot = i + 1
            for j in range(i + 1, len(num_str)):
                if num_str[j] >= num_str[pivot]: # 从i+1的位置往后找最大的一个数 有相等的数且越往后越好(>=)
                    pivot = j
            for k in range(i + 1):               # 从[0,i]找第一个比pivot小的数 两数交换
                if num_str[k] < num_str[pivot]:
                    num_str[k], num_str[pivot] = num_str[pivot], num_str[k]
                    return int("".join(num_str)) # 注意这里的写法 --> "".join(List)
    return num

# variant: given an integer array num. Rearrange th digits to build the second largest num.
# return the 2nd largest value, or empty array if impossible.
''' 思路
1. 构建最大数:先从大到小排列数字 这就是最大的排列 
2. 构造次大数:从最大数中 从后往前找第一个相邻不同的数字 交换它们 这样能得到字典序次大的组合（贪心方式构造第二大）
3. 返回构造结果:交换完后直接返回.如果所有数字都相同 则无法生成次大排列 返回[]
'''
def find_second_largest_num(num:list[int]) -> list[int]:
    if not num or len(num) < 2:
        return []
    counter = collections.Counter(num)
    largest = []
    for i in range(9, -1, -1):
        for j in range(counter[i]):
            largest.append(i)
    k = len(largest) - 1
    while k:
        if largest[k - 1] != largest[k]:
            largest[k - 1], largest[k] = largest[k], largest[k - 1]
            return largest
        k -= 1
    return []

# test
num1 = [2, 7, 3, 6] # [7, 6, 2, 3]
num2 = [1, 2, 1, 1, 1] # [1, 2, 1, 1, 1]
num3 = [1,1,1]
# print(find_second_largest_num(num3))