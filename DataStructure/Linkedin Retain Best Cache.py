'''
给定几个类的定义 实现一个cache. 类似一个LRU.
'''
import heapq

# start given class defination
class K:
    def __init__(self):
        pass

class Rankable:
    def getRank() -> int:
        pass

class DataSource:
    def get(key: K) -> Rankable:
        pass
# end given class defination

class Item:
    def __init__(self, key: K, val: Rankable):
        self.key = key
        self.val = val
    
    def __lt__(self, other: 'Item'):
        return self.val.getRank() < other.val.getRank()

class RetainBestCache:
    def __init__(self, data_source: DataSource, entries_to_retain: int):
        self.data_source = data_source
        self.cache_size = entries_to_retain
        self.cache = dict()
        self.pq = heapq.heapify([])

        pass

    def get(self, key: K) -> Rankable:

        pass
