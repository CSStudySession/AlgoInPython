import collections

class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.size = size # 队列目标长度(非实际长度)
        self.total = 0   # 队列内数值之和
        

    def next(self, val: int) -> float:
  
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.total += val
            return self.total / len(self.queue)
        else:
            removal = self.queue.popleft()
            self.queue.append(val)
            self.total = self.total - removal + val
            return self.total / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)