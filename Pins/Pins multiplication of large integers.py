'''
给定一个或多个由整数数组表示的大整数 每个整数的每一位是一个数组元素(从高位到低位排列) 完成如下操作:
part1:
输入：一个大整数 digits1(如 [1,0,0]），一个单位整数 digit2(如 3)
输出：乘积结果的数组（如 [3,0,0])
part2:
输入：两个大整数（如 [1,0,0] 和 [1,2])
输出：两者乘积的结果数组（如 [1,2,0,0])
part3:
输入：一组大整数数组（如 [[1,0,0], [2], [1,2], [2,0,0]])
输出：全部整数连乘之后的数组结果（如 [4,8,0,0,0,0])
Clarifications
- 大整数可以有trailing 0 但没有leading 0
- 所有输入数字非负
- 输入中可能存在[0],只要有一个[0] 结果就是[0]
- 输入列表中至少有一个非零数组
'''

'''
part1
从最低位向高位逐位相乘, 每次计算乘积并累积进位, 最后处理最高位进位.注意要逆序处理 最后结果再翻转回来
T(n) S(1)
'''
from typing import List
def multiply_single_digit(digits: List[int], digit: int) -> List[int]:
    if digits == [0] or digit == 0:
        return [0]
    carry = 0
    result = []
    n = len(digits)
    idx = n - 1
    # 从低位到高位（逆序处理）
    while idx >= 0:
        prod = digits[idx] * digit + carry
        result.append(prod % 10)
        carry = prod // 10
        idx -= 1
    if carry:
        result.append(carry)
    result.reverse() # 此时 result 是低位在前的，需要翻转
    return result

'''
part 2
通过两个数字从低位到高位逐位相乘并处理进位。
- 预分配结果数组：
   - 两数相乘最多有 len(num1) + len(num2) 位，所以直接分配这么长的数组 result。
- 从低位开始两两相乘：
  - 遍历 num1 和 num2 的每一位（从后往前），将 num1[i] * num2[j] 的结果
    加到 result[i + j + 1]（对应的低位位置），再处理进位加到 result[i + j]。
- 统一处理进位：
  - 每次乘积后都加到对应位置，并立即处理进位，这样最终只需去除前导 0。
- 去除前导零：
遍历结果数组，跳过前导零，得到最终乘积。
T(n*m) S(m+n)
'''
def multiply_two_numbers(num1: List[int], num2: List[int]) -> List[int]:
    if num1 == [0] or num2 == [0]:
        return [0]

    n, m = len(num1), len(num2)
    result = [0] * (n + m)

    # 从末尾开始模拟列竖式乘法
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mul = num1[i] * num2[j]
            p1, p2 = i + j, i + j + 1
            # 加上当前乘积 + 原有的值
            total = mul + result[p2]
            result[p2] = total % 10
            result[p1] += total // 10

    # 去除前导 0
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1
    return result[start:]

# test
# 测试用例 1：12 * 3 = 36
assert multiply_two_numbers([1, 2], [3]) == [3, 6]
# 测试用例 2：99 * 99 = 9801
assert multiply_two_numbers([9, 9], [9, 9]) == [9, 8, 0, 1]
# 测试用例 3：0 * 1234 = 0
assert multiply_two_numbers([0], [1, 2, 3, 4]) == [0]
# 测试用例 4：123 * 456 = 56088
assert multiply_two_numbers([1, 2, 3], [4, 5, 6]) == [5, 6, 0, 8, 8]

'''
part3
多个数连乘可以用pairwise合并, 优先合并最短和最长(减少位运算总数)
每轮合并都调用上面的两数乘法, 最终只剩一个结果
用min-heap做个优化 优先选择length小的两个数相乘进行合并 避免很早产生很长的中间结果
heap上面存(len(d), d), d是当前的数
k:# of lists, M:# of digits of final results. T(k*logk + M^2)  S(k + M)
'''
import heapq
def multiply_multiple_numbers(digit_lists: List[List[int]]) -> List[int]:
    if not digit_lists:
        return [1]  # 空乘积为1
    if len(digit_lists) == 1:
        return digit_lists[0]

    # 转为堆：元素为 (长度, 数字列表)
    heap = [(len(d), d) for d in digit_lists]
    heapq.heapify(heap)

    while len(heap) > 1:
        # 每次取两个最短的
        _, a = heapq.heappop(heap)
        _, b = heapq.heappop(heap)
        prod = multiply_two_numbers(a, b)
        heapq.heappush(heap, (len(prod), prod))
    return heap[0][1]