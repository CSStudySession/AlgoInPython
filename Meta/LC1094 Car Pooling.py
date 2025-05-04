

def car_pooling_0(trips: list[list[int]], capacity: int) -> bool:
    ppl_cnt = [0] * 1001  # 在第i公里有几人上/下车

    for num, start, end in trips:
        ppl_cnt[start] += num  # 上车
        ppl_cnt[end] -= num    # 下车
    
    for cnt in ppl_cnt:
        capacity -= cnt   # 当前location车上乘客总数
        if capacity < 0:
            return False  # 超载
    return True


def car_pooling_1(self, trips: list[list[int]], capacity: int) -> bool:
    events = []
    # 拆分成事件列表
    for numPassengers, start, end in trips:
        events.append((start, numPassengers))   # 上车
        events.append((end, -numPassengers))    # 下车
    # 排序：先按位置升序，再按乘客变化（下车在前）
    events.sort()
    current = 0  # 当前车上人数
    for _, change in events:
        current += change
        if current > capacity:
            return False
    return True