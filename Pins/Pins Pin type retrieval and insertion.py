'''
设计一个数据结构，支持：
根据 pin 类型检索 top-k scored pins(得分最高的 k 个 pin)
支持 pin 插入操作
输入数据格式：
每个 pin 是一个结构体 / 元组，有以下字段：
(id: int, score: float, type: str)
例子：
[
  (id: 0, score: 0.7, type: Static),
  (id: 1, score: 0.5, type: Idea),
  ...
]
Clarification:
id: 范围为 [0, ∞)，唯一
score: 区间 [0, 1]
type: 枚举值 {Static, Idea}
不存在重复 pin(id 唯一)
pin 列表大小 < 1000(初始数据)
每次最多检索 100 个
每个类型的 pin 数量 ≥ 100(可放心检索)

思路:
建立一个dict, key是PinType(一个枚举类型) value是一个max heap(用min heap + nlargest() 模拟 max heap)
插入操作直接 heappush 到对应类型的 heap 中
获取top-k 用 heapq.nlargest(k, heap)，时间复杂度 O(M log k) M 为该类型的 pin 个数
'''
import heapq
from enum import Enum
from collections import defaultdict

# 枚举 pin 类型
class PinType(Enum):
    STATIC = 0
    IDEA = 1

# Pin 类
class PinObj:
    def __init__(self, id: int, score: float, type: PinType):
        self.id = id
        self.score = score
        self.type = type

class PinStore:
    def __init__(self, initial_pins: list):
        self._map = defaultdict(list) # key:type val:list of PinObj
        for pin in initial_pins:
            self.insert_pin(pin)

    def insert_pin(self, pin: PinObj): # T(1)
        self._map[pin.type].append(pin)
    # n:# of pins. T(nlogk + k) S(n+k) 
    def get_top_k_pins(self, k: int, pin_type: PinType):
        all_pins = self._map[pin_type]
        min_heap = []

        for pin in all_pins:
            if len(min_heap) < k:
                heapq.heappush(min_heap, (pin.score, pin.id, pin))
            else:
                if pin.score > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (pin.score, pin.id, pin))
        ret = []
        for _, id, _ in min_heap: # 取出heap中的id
            ret.append(id)
        return ret


'''
Follow-up Questions / Variations
- 扩展到 10 亿个 pin、100 个 pin 类型时：
  - 分布式存储结构(shard by pin type)
  - 每个节点维护一个类型或一组类型的heap
  - 用pin_type + partition key(比如用pin_id%机器数量)定位访问的节点
- 如何异步处理插入 / 查询：
使用异步队列处理插入请求
  - 查询优先返回已有数据，插入数据延迟可接受
  - 需要权衡 eventual consistency 和实时性
- 在高并发插入和查询场景下：
  - 用读写锁/并发 safe 的数据结构
  - 可使用 thread-safe heap 或加锁的 queue
'''



