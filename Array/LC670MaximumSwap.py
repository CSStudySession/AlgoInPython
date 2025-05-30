import collections
'''思路:
1. 从左往右找第一个“低谷”位置x 使得num_str[x] < num_str[x + 1]
含义：找到第一个递增的地方 说明右边可能有更大的数可以换 从这个位置开始我们尝试放一个更大的数过去
从左边找是为了尽早改变高位 高位换得越大 最终数值越大
2. 从x之后向右扫描 找一个值最大且位置最靠后的数z (>= 当前最大 越后越好)
含义：我们想用尽量大的数来换高位 但要保证是最优的（右侧最大且越靠后越优，以便靠前位尽可能大）
选最靠后的位置 因为之后会换一个小的数字过去 靠后对整体影响小
3. 从左往右找第一个比z小的位置y 交换z和y
含义:把最大数z换到最高位(第一个比它小的位置) 产生最大数值变化
注意只需要换一次 题目只允许swap一次
4. 如果整个数字已经是降序排列，无法让它变大，直接返回原数
T(N) S(N)
'''
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
        for _ in range(counter[i]):
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