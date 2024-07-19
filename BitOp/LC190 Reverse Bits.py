
'''
https://leetcode.com/problems/reverse-bits/
(位运算) time: O(1)
使用位运算 n >> i & 1 可以取出 n 的第 i 位二进制数。
从小到大依次取出 n 的所有二进制位，然后逆序累加到另一个无符号整数中。

时间复杂度分析：所有位运算的计算量都是1，比如 n >> 10，将 n 右移10位，计算量是1而不是10。
所以在该问题中，我们总共进行了 4 * 32 次运算(左移 右移 &1 相加, 四个简单运算)，所以时间复杂度是 O(1)
'''
def reverseBits(self, n: int) -> int:
    ret = 0
    for i in range(32):
        ret = ret * 2 + ( (n >> i) & 1)
    return ret

def min_ticket_cost(departure, return_tickets):
    n = len(departure)
    if n == 0:
        return 0

    min_cost = float('inf')
    min_return = float('inf')

    for i in range(n - 1, -1, -1):
        # 更新最小返程票价格
        min_return = min(min_return, return_tickets[i])
        
        # 计算当前出发日期的最小总成本
        current_cost = departure[i] + min_return
        
        # 更新全局最小成本
        min_cost = min(min_cost, current_cost)

    return min_cost

# 测试
departure = [10, 3, 10, 9, 3]
return_tickets = [4, 20, 6, 7, 10]
print(min_ticket_cost(departure, return_tickets))  # 应输出 9
