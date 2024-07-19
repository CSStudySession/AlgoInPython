# Given a list of numbers (0-9) arrange the numbers in the second greatest number

from typing import List
from collections import Counter

def find_sencond_largest(nums: List[int]) -> int:
    # 将数字转换为字符串并计数
    counter = Counter(num for num in nums)
    max_digit, min_digit = -1, 10
    
    # 找最大和最小的digit
    for key in counter.keys(): 
        max_digit = max(max_digit, key)
        min_digit = min(min_digit, key)
    
    # 特判: 最大digit是0 直接返回0
    if max_digit == 0:
        return 0
    
    # 构建最大可能的数
    max_num  = []
    for num in range(max_digit, min_digit - 1, -1):
        if num in counter:
            cur = [num] * counter[num]
            max_num.extend(cur)

    # 从右向左查找第一个可以减小的数字
    pivot = -1
    for i in range(len(max_num) - 1, 0, -1):
        if max_num[i - 1] > max_num[i]:
            pivot = i - 1

        if pivot != -1 and not (max_num[i] == 0 and i - 1 == 0):  # 注意如果是first digit, 不能跟后面的0交换 要not判断一下
            max_num[i - 1], max_num[i] = max_num[i], max_num[i - 1]
            return int(''.join([str(s) for s in max_num]))
    return int(''.join(max_num))

print(find_sencond_largest([5,3,2,5,5,7,9,8])) 
print(find_sencond_largest([9,8,7,6,5,4,3,2,1,0])) 
print(find_sencond_largest([1,2,3,4,5]))
print(find_sencond_largest([1,1,0,0,0])) 