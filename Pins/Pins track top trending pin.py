'''
每条Pin有一个 trending score  需要实现一个功能:
- 跟踪用户最近查看过的Pins(有时间窗口 如过去一周/24小时)
- 在任意时间点返回这段时间内score最高的Pin
输入:一系列包含 pin_id, score, timestamp 的记录
操作：
- add_new_pin(pin_id, score, timestamp)：添加用户查看的新 pin
- remove_expired_pin(current_time)：清理时间窗口之外的 pin
- get_top_scoring_pin()：获取当前窗口中 score 最高的 pin
输出: get_top_scoring_pin() 返回的是 pin_id
Clarification:
- 时间窗口默认是最近的一周(可以变为最近5分钟 5小时等)
- 可能存在多个相同pin_id 出现在不同时间 因此每条记录是独立的
- 输入的pin_score 示例是dict构成的list 每个dict一个键值对 e.g.:
{"981292206280418755": 50}
'''
'''
思路:用max heap实现. 将heap的元素定义为 (score, timestamp, pin_id) 的三元组
用负score构建最大堆(heapq 默认是最小堆)
'''
import heapq
class PinTrendTracker:
    def __init__(self, time_window_secs):
        self.time_window = time_window_secs
        self.pin_heap = []  # 最大堆，元素为 (-score, timestamp, pin_id)
    # T(logn)
    def add_new_pin(self, pin_id, score, timestamp): # 添加新pin到堆中
        heapq.heappush(self.pin_heap, (-score, timestamp, pin_id))
    # T(nlogn) worst when all items expired.
    def remove_expired_pins(self, current_time): # 移除时间窗口之外的 pin
        while self.pin_heap and current_time - self.pin_heap[0][1] > self.time_window:
            heapq.heappop(self.pin_heap)
    # amertized T(1), single time could be T(nlogn) worst.
    def get_top_scoring_pin(self, current_time): # 获取时间窗口内的最高 scoring 的 pin
        self.remove_expired_pins(current_time)
        if self.pin_heap:
            return self.pin_heap[0][2]  # 返回pin_id
        return None

'''
followup: return top score from last N pins.
思路: 1.用deque存last N items.超过个数N的 popleft()掉. 2.max heap维护heap中的items.注意每次要判断堆顶是否过期.
'''
from collections import deque
import heapq
class TopPinTracker:
    def __init__(self, max_size):
        self.max_size = max_size
        self.recent_pins = deque()  # 存储最近N个 (timestamp, pin_id, score)
        self.max_heap = []  # 堆中存储 (-score, timestamp, pin_id)
        self.expired_set = set()  # 存储已被deque删除的 pin 唯一标识
    
    # T(logn) for heappush()
    def add_new_pin(self, pin_id, score, timestamp):
        self.recent_pins.append((timestamp, pin_id, score))
        heapq.heappush(self.max_heap, (-score, timestamp, pin_id))

        if len(self.recent_pins) > self.max_size:
            old = self.recent_pins.popleft()
            # 标记为已过期
            self.expired_set.add((old[0], old[1]))  # (timestamp, pin_id)
    
    # if k items expired, total n items, T(k*logn)
    def get_top_scoring_pin(self):
        # 从堆中弹出所有已过期元素 直到第一个不过期的 就返回
        while self.max_heap:
            _, ts, pid = self.max_heap[0]
            if (ts, pid) in self.expired_set:
                heapq.heappop(self.max_heap)
                self.expired_set.remove((ts, pid))
            else:
                return pid
        return None