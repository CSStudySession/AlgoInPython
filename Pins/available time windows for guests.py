'''
https://leetcode.com/company/pinterest/discuss/5526021/Pinterest-or-Onsite-or-Bay-Area-or-Meeting-rooms-variation
You're a restaurant manager who's job is to find available time windows for seating N number of guest(s). 
Lets assume your restaruant is specified in the following way:

restaurant = {
    'restaurant_start': 9,
    'restaurant_end': 22,
    'capacity': 5,
    'reservations': [
        {'start': 10, 'end': 14, 'ppl': 3},
        {'start': 11, 'end': 13, 'ppl': 2},
        {'start': 13.5, 'end': 15, 'ppl': 1},
        {'start': 16, 'end': 20, 'ppl': 2}
    ]
}
Where restaurant_start and restaurant_end are the open and close times of the resturant, 
capacity is the maximum number people the restaurant can fit at any point, 
and reservations are existing reservations w/ guests 
(e.g ppl is the number of customers who are already at the restaurant at that time interval).

Write an algorithm that can output all available time intervals for seating an input N guests 
from restaurant open to close (e.g [[9,11],....]]). 
Assume your input to the function is in the format of the restaurant dictionary object 
specified above along with a parameter N indicating the number of people to seat.

思路: heap
1. 遍历每个预订信息 把每个预订的开始时间start和结束时间end分别作为堆中的事件处理。
堆中的每个元素是一个 [time, seats] 对，表示某个时间点 time 和该时间点发生的座位变化 seats
正数表示增加座位，负数表示减少座位。
返回处理后的事件堆，包含所有预订的开始和结束时间点。
2. 遍历时间堆 检查每个时间段是否可以容纳n人。如果可以 记录这个时间段。
在遍历的过程中 通过更新当前容量cur_cap来实时跟踪可用座位情况。
遍历结束后 如果最后一个事件后的时间段依然可以容纳n人 则将其加入结果列表。

时间复杂度: O(m*logm) 其中m是预订信息的数量
空间复杂度: O(m)
'''
from typing import List
import heapq

class ReservationScheduler:

    def __init__(self, restaurant:dict):
        self.time_slots_heap = self.get_time_slots_for_heap(restaurant['reservations'])
        self.cap = restaurant['capacity']
        self.opening = restaurant['restaurant_start']
        self.close = restaurant['restaurant_end']
        self.cur_cap = restaurant['capacity']

    def get_time_slots_for_heap(self, reservations:List[dict]) -> List[List[int]]:

        heap = []
        for res in reservations:
             # 负号因为 来人的时候需要从current_capacity中减掉res['ppl']
            heapq.heappush(heap, [res['start'], -res['ppl']])
             # 人走的时候需要从current_capacity中加上res['ppl']
            heapq.heappush(heap, [res['end'], res['ppl']])
        return heap

    def all_available_time_slots_seating_N_seating(self, n):

        if n > self.cap:
            return []

        available_intervals = []

        prev = self.opening
        cur_cap = self.cap
        heap_copy = self.time_slots_heap.copy()
        while heap_copy:
            time, seats = heapq.heappop(heap_copy)
            # 如果当前时间 time 大于 prev（上一个时间点），且当前可用座位数 cur_cap 大于或等于 n，
            # 那么 [prev, time] 之间的时间段可以容纳 n 人，将其加入 result 列表。
            if time > prev and cur_cap >= n:
                available_intervals.append([prev, time])
            # 更新座位和时间
            cur_cap += seats
            prev = time

        # 如果堆中最后一个事件的时间点prev 早于餐厅关闭时间 self.close，
        # 说明在这个事件之后到餐厅关闭之间仍有可用时间段
        if prev < self.close:
            available_intervals.append([prev, self.close])

        # merge intervals in available_intervals
        # 可用的time intervals 很可能有重叠: 
        # 比如可能出现[[18, 19],[19, 22]] 两个区间是相邻的 可以合并为 [[18, 22]]
        ret = []
        if available_intervals:
            start = available_intervals[0][0]
            end = available_intervals[0][1]
            
            for interval in available_intervals[1:]:
                if end >= interval[0]:
                    end = max(end, interval[1])
                else:
                    ret.append([start, end])
                    start = interval[0]
                    end = interval[1]
            ret.append([start, end])
        return ret
    
# unit test
restaurant = {
    'restaurant_start': 9,
    'restaurant_end': 22,
    'capacity': 5,
    'reservations': [
        {'start': 10, 'end': 14, 'ppl': 3},
        {'start': 11, 'end': 13, 'ppl': 2},
        {'start': 13.5, 'end': 15, 'ppl': 1},
        {'start': 16, 'end': 20, 'ppl': 2}
    ]
}
rs = ReservationScheduler(restaurant)
print(rs.all_available_time_slots_seating_N_seating(5))

'''
https://www.1point3acres.com/bbs/thread-998365-1-1.html
跟上面的题类似 变种
Input:
Store Open and close time , total capacity, List of existing reservations
Output every interval with the capacity available

Test Case 1:
Open: 8 AM, Close 9 PM, Capacity: 5
Reservations { 
    {
        start time: 9 am
        end time: 9:30 am
        size : 3
    }
}

Output case 1: Map<Interval, Int>
8AM-9AM 5,
9-930AM 2,
930-9PM 5

Test case example 2:
Reservations { 
    {
‍‌‍‍‍‌‍‍‌‌‌‌‌‌‍        start time: 9 am
        end time: 9:30 am
        size: 3
    },
    {
        start time: 9:15 am
        end time : 9:45 am
        size: 2
    }
}

Output case 2:   Map<Interval, Int>
8:00AM-9:00AM 5,
9:00AM-9:15AM 2,
9:15AM-9:30AM 0,
9:30AM-9:45AM 3
9:45AM-9:00PM 5

思路：
1. 将每个预订的开始时间和结束时间转化为时间事件，并将其存入堆中。开始时间表示减少座位数，结束时间表示增加座位数。
2. 我们通过遍历时间堆，逐段计算每个时间区间内的可用容量，并记录在 result 字典中。
3. 如果最后一个时间事件的时间点未到达商店关闭时间，需处理剩余的时间段

时间复杂度为 O(m log m) m是预订数量
空间复杂度为 O(m)
'''

import heapq

class StoreScheduler:
    def __init__(self, store_start: str, store_end: str, capacity: int, reservations: list):
        self.capacity = capacity
        self.opening = self.time_to_minutes(store_start)
        self.closing = self.time_to_minutes(store_end)
        self.time_slots_heap = self.get_time_slots_for_heap(reservations)

    def time_to_minutes(self, time_str: str) -> int:
        """将时间字符串转化为分钟数"""
        time_parts = time_str.split(' ')
        hour, minute = map(int, time_parts[0].split(':'))
        if 'PM' in time_parts[1] and hour != 12:
            hour += 12
        elif 'AM' in time_parts[1] and hour == 12:
            hour = 0
        return hour * 60 + minute

    def minutes_to_time(self, minutes: int) -> str:
        """将分钟数转化为时间字符串"""
        hour = minutes // 60
        minute = minutes % 60
        period = 'AM' if hour < 12 else 'PM'
        if hour == 0:
            hour = 12
        elif hour > 12:
            hour -= 12
        # :02d的作用->d:整数 2:至少占用两个字符宽度 0:少于两个字符长度时 在前面补零
        return f"{hour}:{minute:02d} {period}"

    def get_time_slots_for_heap(self, reservations: list) -> list:
        heap = []
        for res in reservations:
            start = self.time_to_minutes(res['start time'])
            end = self.time_to_minutes(res['end time'])
            size = res['size']
            heapq.heappush(heap, [start, -size])
            heapq.heappush(heap, [end, size])
        return heap

    def available_capacity_intervals(self) -> dict[str, int]:
        result = {}
        heap = self.time_slots_heap.copy() # 创建堆的副本，避免修改原始数据

        prev = self.opening
        cur_cap = self.capacity

        while heap:
            time, change = heapq.heappop(heap)
            
            # 注意下面这里一定要写成">" 不能">=". 有可能出现同一个时间点 有两个事件的情况
            if time > prev:
                result[f"{self.minutes_to_time(prev)}-{self.minutes_to_time(time)}"] = cur_cap
            cur_cap += change
            prev = time

        # 处理营业时间结束前的最后一个时间段
        if prev < self.closing:
            result[f"{self.minutes_to_time(prev)}-{self.minutes_to_time(self.closing)}"] = cur_cap
        return result
    
    # 题目如果要求只输出容量大于或等于k的时间段
    def available_capacity_intervals_for_K(self, k) -> dict[str, int]:
        result = {}
        heap = self.time_slots_heap.copy() # 创建堆的副本，避免修改原始数据

        prev = self.opening
        cur_cap = self.capacity
        
        # 用来跟踪上一个有效时间段的结束时间。
        # 有助于我们合并连续的有效时间段。
        last_valid_time = self.opening

        while heap:
            time, change = heapq.heappop(heap)
            if time > prev:
                if cur_cap >= k:
                    if prev > last_valid_time:
                        result[f"{self.minutes_to_time(prev)}-{self.minutes_to_time(time)}"] = cur_cap
                    else:
                        result[f"{self.minutes_to_time(last_valid_time)}-{self.minutes_to_time(time)}"] = cur_cap
                    last_valid_time = time
                elif prev < last_valid_time:
                    result[f"{self.minutes_to_time(last_valid_time)}-{self.minutes_to_time(prev)}"] = result.get(f"{self.minutes_to_time(last_valid_time)}-{self.minutes_to_time(prev)}", cur_cap)
                    last_valid_time = prev
            cur_cap += change
            prev = time

        # 处理营业时间结束前的最后一个时间段
        if prev < self.closing and cur_cap >= k:
            if prev > last_valid_time:
                result[f"{self.minutes_to_time(prev)}-{self.minutes_to_time(self.closing)}"] = cur_cap
            else:
                result[f"{self.minutes_to_time(last_valid_time)}-{self.minutes_to_time(self.closing)}"] = cur_cap
        return result

# unit test
scheduler1 = StoreScheduler("8:00 AM", "9:00 PM", 5, [
    {'start time': '9:00 AM', 'end time': '9:30 AM', 'size': 3}
])
output1 = scheduler1.available_capacity_intervals()
print(output1)

scheduler2 = StoreScheduler("8:00 AM", "9:00 PM", 5, [
    {'start time': '9:00 AM', 'end time': '9:30 AM', 'size': 3},
    {'start time': '9:15 AM', 'end time': '9:45 AM', 'size': 2}
])
output2 = scheduler2.available_capacity_intervals()
print(output2)

scheduler3 = StoreScheduler("8:00 AM", "9:00 PM", 5, [
    {'start time': '9:00 AM', 'end time': '10:00 AM', 'size': 2},
    {'start time': '9:30 AM', 'end time': '10:00 AM', 'size': 3}
])
output3 = scheduler3.available_capacity_intervals()
print(output3)