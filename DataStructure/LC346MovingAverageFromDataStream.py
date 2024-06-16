import collections

class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.queue()
        self.size = size
        self.total = 0
        

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