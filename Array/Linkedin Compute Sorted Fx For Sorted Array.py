'''
given sorted array A of doubles. compute a new sorted array B where each element
is obtained by applying the following fuction F(x) (x is element in A)
f(x) = ax^2 + bx + c, where a > 0
output: array B of sorted doubles f(x)

parabola with a > 0, 开口向上的抛物线. 最小值=-b/(2a) 根据图像法: 在最小值左边单调减 在最小值右边单调增
分成两部分算 得到两个array 然后转化成 merge two sorted array
time complexity: O(n) -> 沿抛物线算两个f_x数组O(n), merge two sorted list O(n)
'''

from typing import List
def compute_sorted_fx(nums: List[float], a:float, b:float, c:float) -> List[float]:
    if (a <= 0):
        raise ValueError("input a should be >= 0")

    min_val = -b / (2*a)
    left_arr, right_arr = [], []

    for i in range(len(nums)):
        f_x = a * (nums[i] ** 2) + b * nums[i] + c
        if nums[i] <= min_val:        # parabola左边 left_arr单调减小
            left_arr.append(f_x)
        else:
            right_arr.append(f_x)     # parabola右边 right_arr
    
    # 下面是merge two sorted list的模板
    out_arr = []
    left_idx, right_idx = len(left_arr) - 1, 0    # 注意left是从后往前数 要注意单调性
    while left_idx >= 0 and right_idx < len(right_arr): # 写while循环注意在循环逻辑最后把对应的idx++/--
        if left_arr[left_idx] <= right_arr[right_idx]:
            out_arr.append(left_arr[left_idx])
            left_idx -= 1
        else:
            out_arr.append(right_arr[right_idx])
            right_idx += 1
    
    while left_idx >= 0:
        out_arr.append(left_arr[left_idx])
        left_idx -= 1
    while right_idx < len(right_arr):
        out_arr.append(right_arr[right_idx])
        right_idx += 1
    
    return out_arr

# unit test
a = 2.0
b = -20.0
c = 1.0
nums = [-13, -10, -3, 1, 2, 3, 4, 5, 6, 7, 20, 50]

print(compute_sorted_fx(nums, a, b, c))