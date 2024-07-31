'''
Given billions of training data in a file. Each data has one of 4 class labels.
Output:
select M_i data from each class, where i in {1, 2, ..., 4}

Example: 
feature in json format   lable
{"user": 1, features}    Blue
{"user": 2, features}    Red
...

M_i requires: {100 of Blue, 200 of Red, 300 of Green, 400 of Orange}

optimal solution: resovior sampling
其它可能解:
1. assign a random number to each data, sort and take the top M. 
 - works only if all data can be fit into memory
 - time complexity O(nlogn) slower than reservior sampling O(n)

2. Iterate thru all data and select each one with probability M/N.
 - N is not guaranteed known or given in some cases, so it may require another loop to count N.
 - since it takes data with probility M/N, so in the end it may not result exact M records. 
'''
from typing import List
from collections import defaultdict
import random

class Instance:
    def __init__(self, label: str = ""):
        self.label =label

class InstanceIterator:
    def __init__(self, start, end):
        self.cur = start
        self.end = end
    def has_next() -> bool:
        pass
    def next() -> Instance:
        pass
    
def sampling(iterator: InstanceIterator, requirement: dict[str, int]) -> dict[str, List[Instance]]:
    ret = defaultdict(list)
    counter = defaultdict(int)

    while iterator.has_next():
        cur_ins = iterator.next()
        cur_label = cur_ins.label

        cur_cnt = len(ret[cur_label])
        cur_num = counter[cur_label]

        if cur_cnt < requirement[cur_label]:  # 蓄水池还没满 直接放到对应的list里面
            ret[cur_label].append(cur_ins)
        else:                                 # 蓄水池满 生成一个[0,cur_num]之间的索引j   
            idx = random.randint(0, cur_num)
            if idx < requirement[cur_label]:  # 如果j小于threshold 用当前元素替换下标为j的元素
                ret[cur_label][idx] = cur_ins
        
        counter[cur_label] = cur_num + 1      # 更新cur_num 
    
    return ret

'''
followup: how to do it using distributed computing framework like Hadoop?
1. 从输入文件加载数据。
2. 为每条记录生成一个随机数。
3. 根据生成的随机数对记录进行排序。
4. 从排序后的记录中选择前 M 条记录，作为最终的随机样本。
----
examples = load '$input' using PigStorage();
examples = foreach examples generate id, RAMDOM(), as rnd;
sample = order Examples by rnd;
sample = limit sample $M;
----
'''