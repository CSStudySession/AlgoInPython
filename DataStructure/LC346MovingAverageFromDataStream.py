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

'''
variant1: given a list of int nums and an int size, compute the avg of elements
in a sliding window of exactly size elements. return a list containing the ret of 
computations.
重点:array大小固定 不是streaming input. 直接双指针维护滑动窗口即可.
T(n) S(1)
'''
def calc_avg_of_window(nums:list[int], size:int) -> list[int]:
    ret = []
    if size > len(nums) or size <= 0:
        return ret
    window_sum = 0
    left, right = 0, 0
    while right < len(nums):
        window_sum += nums[right]
        if right - left + 1 == size:
            ret.append(window_sum // size)
            window_sum -= nums[left]
            left += 1
        right += 1
    return ret

nums = [5, 2, 8, 14, 3]
size = 3 # [5,8,8]
nums = [6]
size = 1 # [6]
nums = [2, 4, 6, 8, 10, 12]
size = 1 
# print(calc_avg_of_window(nums, size))

'''
variant2: given a list of int nums,在大小为k的滑动窗口内,求every other number的平均
(不是所有数的平均值)
思路:用两个队列even and odd queue, 分别存储下标是偶数和奇数的元素. 移动过程中维护even and odd sum.
当窗口大小>=k时 根据窗口左端点idx-k+1的奇偶性 计算average 并更新对应的sum和队列.
T(n) S(k)
'''
def cal_moving_avg_every_other_num(nums:list[int], k: int) -> list[int]:
    ret = []
    if not nums or k <= 0 or k > len(nums):
        return ret
    even_queue, odd_queue = collections.deque(), collections.deque()
    even_sum, odd_sum = 0, 0
    for idx in range(len(nums)):
        if idx % 2 == 0: # 根据下表奇偶性 入不同队列并更新相应sum
            even_queue.append(nums[idx])
            even_sum += nums[idx]
        else:
            odd_queue.append(nums[idx])
            odd_sum += nums[idx]
        if idx >= k - 1: # 窗口大小等于k了
            left = idx - k + 1 # 窗口左端点的下标left
            if left % 2 == 0: # 根据奇偶性 取对应的sum算均值 并移除队列最远的元素
                ret.append(even_sum // k)
                even_sum -= even_queue.popleft()
            else:
                ret.append(odd_sum // k)
                odd_sum -= odd_queue.popleft()
    return ret