'''
有面经提到: "有点像splitwise payer和payee怎么清算"
You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] 
indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

Return the minimum number of transactions required to settle the debt.

Example 1:
Input: transactions = [[0,1,10],[2,0,5]]
Output: 2
Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:
Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
Output: 1
Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.

思路: 见解析 https://github.com/happygirlzt/algorithm-illustrations/blob/master/465.%20Optimal%20Account%20Balancing.png
backtracking problem

记M为有非零余额的账户数
dfs函数的最坏情况下会遍历所有可能的状态组合。由于每个余额可以进行 M 次状态变化（选择不同账户结算），所有的状态组合数量是 O(M!)。
再考虑到每次 dfs 调用中的循环(for i in range(1, len(balances))），其复杂度为 O(M)，因此最坏情况下的递归调用次数为 O(M * M!)。
总体上，时间复杂度大约为 O(M * M!)。
递归的最大深度是O(M)，因此调用栈的空间复杂度为 O(M)
'''
from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        if not transactions:
            return 0

        # trans[i][0]给trans[i][1] 转了trans[i][2]块钱
        # 如果最终想实现平衡(每人里外里收支为零): trans[i][0]需要被给trans[i][2]块钱, trans[i][1]需要给出trans[i][2]块钱 
        book = defaultdict(int)
        for tran in transactions:
            book[tran[0]] = book[tran[0]] + tran[2]
            book[tran[1]] = book[tran[1]] - tran[2]
         
        # 把book中所有非0的values记下来 这些是需要之后再调整到0的balances
        # 如果value本身已经为0 不需要额外调整了 已经balanced
        ref = [] 
        for key in book:
            if book[key]:
                ref.append(book[key])
        
        return self.dfs(0, ref)

    def dfs(self, index:int, ref:List[int]) -> int:
        if index == len(ref): # 调整到头了 需要操作次数为0
            return 0
        
        cur_amnt = ref[index]
        if not cur_amnt:
            return self.dfs(index + 1, ref)

        min_ops = float('inf')           # 初始化一个最小操作次数
        for i in range(index + 1, len(ref)):  # 站在当前的index看 从index+1起每个位置都可以尝试balance操作
            nxt_amnt = ref[i]
            if cur_amnt * nxt_amnt < 0:  # 只有index和i对应的值符号不同时 才可能互相even out
                ref[i] = cur_amnt + nxt_amnt
                min_ops = min(min_ops, 1 + self.dfs(index + 1, ref))
                ref[i] = nxt_amnt   # 注意回溯时要还原现场

                # pruning: 如果index和i对应的值互相刚好balance 对调整index的balance来说 不需要尝试其他可能了 已经是最优解
                if cur_amnt + nxt_amnt == 0:
                    break
        return min_ops