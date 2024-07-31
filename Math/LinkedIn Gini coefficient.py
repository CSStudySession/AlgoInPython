'''
Given a list of connection counts: [0,0,1,1,1,2,3,3,4,5]. connections[i] = x 代表第i个人有x个connections
需要提出一个方法 可以计算出connections的"不均衡性". 

可以提出使用: Gini coefficient:
x-axis: cumulative percent of people
y-axis: cumulative percent of coresponding number, connection number in this case.
A formula: g = 1 - 2*integral(f), where f is the fucntion formed by y-x, should be given.
'''

from collections import defaultdict
from typing import List

def inequality_calculation(connections: List[int]) -> float:
    counter = defaultdict(int)
    mem_cnt = cnct_cnt = 0
    min_num, max_num = float("inf"), float("-inf")

    # 统计各个变量的值
    for num in connections:
        mem_cnt += 1                    # 总人数
        cnct_cnt += num                 # 总connection数
        counter[num] = counter[num] + 1 # 有num个connection的人的个数
        min_num = min(min_num, num)     # 每次更新min/max connection num. 下面会用到
        max_num = max(max_num, num)
    
    if cnct_cnt == 0: # edge case: there's no connects among all people. 下面循环会除cnct_cnt 所以这里要处理掉
        return 0.0

    ret = prev_cnct = 0
    # 计算积分(integral of f). 画图可以看出 每个区间可以看成是一个"梯形"(trapezoid) 即可以转化成梯形面积求和
    for cur_cnct in range(min_num, max_num + 1):
        if cur_cnct not in counter:
            continue
        cur_mem = counter[cur_cnct]
        # trapezoid area formula: (上底+下底)*高/2 注意这里的cnt都要除以总数 作为百分比参与计算
        area = (prev_cnct + cur_cnct) / cnct_cnt * cur_mem / mem_cnt * 0.5
        ret += area
        prev_cnct += cur_cnct   # 要更新prev_cnct数用作下次计算
    
    return (1 - 2 * ret)

connections = [0,0,1,1,1,2,3,3,4,5]
# connections = [0,0,0,1,0,0,1,0,0,0,0,0,0,0]
print(inequality_calculation(connections))