'''
https://leetcode.com/company/pinterest/discuss/5587704/Pinterest-Onsite
A candidate has two sets of score - engagement and relevance score (es and rs respectively). 
Find how many candidates who's engagement and relevance score are greater than K other candidates.
i.e for candidate i -> there must be k candidates where es[i] > es[j] and rs[i] > rs[j]

e.g
es = [1, 2, 3, 4, 5]
rs = [1,2, 3, 4, 5]
K = 1
Output: 4 since all candidates except the 0th one have at least one other candidate 
where its engagement and relevance score is greater than another candidate
Implementation should be in O(n log n)
这道题类似leetcode 1996

思路:优先队列
1.两个优先队列（最小堆）来分别处理 es 和 rs。
每个优先队列中存储一个二元组 (score, index) 其中score是候选人的得分 index是该得分在原数组中的索引。
首先将所有候选人的es和rs逐一加入各自的优先队列中。
2.删除前K个得分最低的候选人
为了删除在es上得分最低的前K个候选人 从es的优先队列中逐个弹出得分最低的元素。
对于每个从es优先队列中弹出的元素 我们也需要从rs优先队列中删除相应索引的元素。并且rs score比当前元素低的值 也需要被删除
3.统计剩余候选人
最后统计rs优先队列中剩下的候选人数量 这个数量就是符合条件的候选人数量。

时间复杂度为 O(n log n)
空间复杂度为 O(n)
'''
import heapq
from typing import List

def find_greater_than_k_others(es:List[int], rs:List[int], k:int) -> int:
    if not es or not rs:
        return -1
    
    # 创建优先队列
    es_pq = []
    rs_pq = []
    
    for i in range(len(es)):
        heapq.heappush(es_pq, (es[i], i))
        heapq.heappush(rs_pq, (rs[i], i))
    
    # 记录删掉元素的下标
    removed = set()
    # 删除前k个得分最低的候选人
    while k:
        es_score, index = heapq.heappop(es_pq)
        if index not in removed:
            while rs_pq and rs_pq[0][1] != index:
                _, popped_index = heapq.heappop(rs_pq)
                removed.add(popped_index)    # 注意这里需要把index加到removed set中
            # 删除对应的rs中的元素
            heapq.heappop(rs_pq)
            removed.add(index)
        k -= 1        
    # 剩余候选人数量即为答案
    return len(rs_pq)


# unit test 1
es1 = [1, 2, 3, 4, 5]
rs1 = [1, 2, 3, 4, 5]
K = 1
print(find_greater_than_k_others(es1, rs1, K))  # 输出: 4

# unit test 2
es2 = [1, 2, 3, 4, 5]
rs2 = [5, 4, 3, 2, 1]
K = 2
print(find_greater_than_k_others(es2, rs2, K))  # 输出: 0