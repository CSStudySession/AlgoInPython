'''
几个人一起出去旅游 有人先垫付了各项费用（如机票、酒店、租车等）现在大家想在旅程结束后公平结算
输入：一个由 transaction 构成的列表，每个 transaction 包括：
payer:垫付人, amount: 总花费金额, payees: 本次花费的受益人列表
例如：
[
  {
    "payer": "Jane",
    "amount": 4000,
    "payees": ["John", "Jane", "Alex", "Adam"]
  },
  {
    "payer": "Alex",
    "amount": 2000,
    "payees": ["Jane", "Alex"]
  }
]
输出:一个数组 每一项是建议的转账方案 使得所有人的花费平均(settle up) 输出结构如:
[
  { "payer": "John", "amount": 1000, "payee": "Jane" },
  { "payer": "Adam", "amount": 1000, "payee": "Jane" }
]
'''
'''
思路:
构建一个dict for net balance
 - 每个人维护一个净值 balance = 付出 - 实际消费
 - 所有人的净值加起来必须为 0
按照贪心策略结算:
 - 找出当前欠最多钱的（负数最多）和被欠最多钱的（正数最多）
 - 从欠钱的人向被欠最多的人转账 金额为两者之间较小值的绝对值
不断更新净值表直到所有人的 balance 为 0
N:人数 T:# of transactions K:avg # of payees(输入中 payee列表的平均长度)
T(nlogn + T*K)   S(N)
'''
from typing import List, Dict
from collections import defaultdict

def get_suggested_payments(transactions: List[Dict]) -> List[Dict]:
    net_balance = defaultdict(float)
    for txn in transactions:
        payer = txn.get('payer')
        amount = txn.get('amount')
        payees = txn.get('payees')
        # Corner case: 无效交易 跳过
        if not payees or amount is None or len(payees) == 0:
            continue
        # 计算每人应负担的金额
        share = amount / len(payees)
        # 垫付人加钱
        net_balance[payer] += amount
        # 每个受益人扣钱
        for person in payees:
            net_balance[person] -= share
    # 分离债务人和债权人
    creditors = []
    debtors = []
    for person, balance in net_balance.items():
        rounded = round(balance, 2)
        if rounded > 0:
            creditors.append([person, rounded])
        elif rounded < 0:
            debtors.append([person, rounded])

    # 排序以进行贪心匹配
    creditors.sort(key=lambda x: -x[1]) # 升序 整数大的在前 
    debtors.sort(key=lambda x: x[1])  # 升序 负数小在前

    result = []
    i = j = 0
    while i < len(debtors) and j < len(creditors):
        debtor, debt_amt = debtors[i]
        creditor, credit_amt = creditors[j]
        # 欠的钱和被欠的钱 取一个绝对值小的
        settle_amt = round(min(-debt_amt, credit_amt), 2)
        result.append({
            'payer': debtor,
            'amount': settle_amt,
            'payee': creditor
        })
        # 更新各自余额
        debtors[i][1] += settle_amt
        creditors[j][1] -= settle_amt
        # 谁的账even了 就移动到下一个位置
        if round(debtors[i][1], 2) == 0:
            i += 1
        if round(creditors[j][1], 2) == 0:
            j += 1
    return result

'''
followup1: 支持按百分比分摊金额(例如一个人只吃了 10% 的菜 三个人不均摊价格 而是按百分比）
思路:首先在输入增加一个字段split, 一个与payees长度相同的比例列表:
{'payer': 'A', 'amount': 100, 'payees': ['A', 'B', 'C'], 'split': [20, 30, 50]}
对应计算每人应付的金额：
share = amount * (split[i] / 100.0)

代码中 在计算net_balance[i]前 加入下面的逻辑:
split = txn.get('split')  # 可能是 None
# 分摊逻辑
if split and len(split) == len(payees):
    shares = [amount * (pct / 100.0) for pct in split]
else: # split有异常 fallback到平均均摊模式
    share = amount / len(payees)
    shares = [share] * len(payees)

for i in range(len(payees)): # update net_balance for each person
    person = payees[i]
    person_share = shares[i]
    net_balance[person] -= person_share
'''

'''
followup2: 如何求最小转账次数?
思路:dfs 尝试所有可能的转账可能 选最小的
记M为有非零余额的账户数
dfs函数的最坏情况下会遍历所有可能的状态组合。
由于每个余额可以进行M次状态变化(选择不同账户结算) 所有的状态组合数量是 O(M!) (NP-hard problem)
再考虑到每次dfs调用中的循环(for i in range(1, len(balances))），其复杂度为 O(M)
因此最坏情况下的递归调用次数为 O(M * M!)。时间复杂度大约为 O(M * M!)。
递归的最大深度是O(M)，因此调用栈的空间复杂度为 O(M)
'''
def get_minimum_transactions(self, transactions: List[dict]) -> int:
    # 构建每个人的净资产
    balance = defaultdict(float)
    for txn in transactions:
        payer = txn.get('payer')
        amount = txn.get('amount')
        payees = txn.get('payees')
        if not payees or amount is None or len(payees) == 0:
            continue
        share = amount / len(payees)
        balance[payer] += amount
        for person in payees:
            balance[person] -= share
    # 提取非0净值（需要结算的人）
    debt_list = [round(val, 2) for val in balance.values() if round(val, 2) != 0]
    return dfs(0, debt_list)

def dfs(index: int, debt: List[float]) -> int:
    # 跳过已平衡的账户
    while index < len(debt) and debt[index] == 0:
        index += 1
    if index == len(debt):
        return 0

    min_ops = float('inf')
    for i in range(index + 1, len(debt)):
        if debt[index] * debt[i] < 0:  # 只能在符号相反的人之间尝试转账
            # 模拟转账
            original = debt[i]
            debt[i] += debt[index]
            min_ops = min(min_ops, 1 + dfs(index + 1, debt))
            debt[i] = original  # 回溯
            # 剪枝：如果正好抵消了，可以直接 break（当前 index 不需要尝试别的路径）
            if debt[i] + debt[index] == 0:
                break
    return min_ops