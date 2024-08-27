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
import threading

class Instance:
    def __init__(self, label: str = ""):
        self.label =label

class InstanceIterator:
    def __init__(self, start, end):
        self.cur = start
        self.end = end
        self.lock = threading.Lock()
    def has_next(self) -> bool:
        with self.lock: # 没要求多线程不写这句
            pass
    def next(self) -> Instance:
        with self.lock: # 没要求多线程不写这句
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

# 下面这版实现 是考虑线程安全 InstanceIterator类 和 sampling方法里 都相应加了锁
class Instance:
    def __init__(self, label: str = ""):
        self.label = label
    # Instance 类不需要任何同步机制
    # 1. 它是不可变的（label 在初始化后不会改变）
    # 2. 每次调用 InstanceIterator.next() 都会创建一个新实例
    # 3. 它没有修改内部状态的方法

class InstanceIterator:
    def __init__(self, start, end):
        self.cur = start
        self.end = end
        self.lock = threading.Lock()  # InstanceIterator 需要锁来保证线程安全

    def has_next(self) -> bool:
        with self.lock:
            return self.cur < self.end

    def next(self) -> Instance:
        with self.lock:
            if self.cur >= self.end:
                raise StopIteration
            instance = Instance(f"Label_{self.cur}")  # 创建新的Instance对象
            self.cur += 1
            return instance

def sampling(iterator: InstanceIterator, requirement: dict[str, int]) -> dict[str, List[Instance]]:
    ret = defaultdict(list)
    counter = defaultdict(int)
    lock = threading.Lock()  # 这个锁用于保护ret和counter

    while True:
        try:
            cur_ins = iterator.next()  # InstanceIterator的next方法已经是线程安全的
        except StopIteration:
            break
        
        cur_label = cur_ins.label  # 访问Instance的label不需要同步

        with lock:
            cur_cnt = len(ret[cur_label])
            cur_num = counter[cur_label]

            if cur_cnt < requirement[cur_label]:
                ret[cur_label].append(cur_ins)
            else:
                idx = random.randint(0, cur_num)
                if idx < requirement[cur_label]:
                    ret[cur_label][idx] = cur_ins
        
            counter[cur_label] = cur_num + 1
    
    return ret