'''
You are given a list of pins (as integer values) and corresponding categories. 
reorder them such that no two pins are places side by side if they belong to the same category.

this is similar to question: https://leetcode.com/problems/reorganize-string/description/

思路：
1.计数和堆构建:通过Counter计算每个类别的频率 并将其按频率存入最大堆（通过存储负值实现最大堆）。
2.核心逻辑：
从堆中取出频率最高的类别，将其插入结果数组。
为了避免相邻 必须先插入其他类别的pin 然后再插入这个频率较高的类别。所以我们在取出类别后，
不立即将其重新放入堆，而是暂时保留，直到下一个类别被处理完。
3.确保正确的排列:我们确保每次都能尽量选择不同的类别 直到所有类别的pin都被插入结果数组为止。

时间复杂度:
总的时间复杂度是O(n log k) n是pins数量 k是不同类别数量
空间复杂度:
最大堆和计数器的空间复杂度都是O(k) 其中k是不同类别的数量。
总的空间复杂度是O(k)。
'''
from typing import List
from collections import Counter
import heapq

def reorder_pins(pins: List[int]) -> List[int]:
    if not pins: 
        return []
    
    len_pins = len(pins)
    # 统计每个类别的出现次数
    count = Counter(pins)
    heap = []
    
    # 将类别和对应的pin按照出现次数推入最大堆（用负值模拟最大堆）
    for category, freq in count.items():
        if freq > (len_pins + 1) // 2:  # 如果某个类别的频率超过(n+1)/2, 则无法重组
            return []
        heapq.heappush(heap, (-freq, category))
    
    res = []
    prev_freq, prev_category = 0, None
    
    while heap:
        # 从堆中取出频率最高的类别
        freq, category = heapq.heappop(heap)
        # 将对应类别的pin插入结果中
        res.append(category)
        
        # 如果上一个类别还有剩余频率，则将它重新放回堆中
        if prev_freq < 0:
            heapq.heappush(heap, (prev_freq, prev_category))
        
        # 更新当前类别的频率
        prev_freq, prev_category = freq + 1, category

    return res

# unit test 1
pins1 = [1, 1, 2, 2, 3, 3, 1, 2]
print(reorder_pins(pins1))  # Example output could be [1, 2, 1, 3, 1, 2, 3, 2]

# unit test 2
pins2 = [1, 2, 1, 3, 1, 4, 1, 5, 1]
print(reorder_pins(pins2))  # Example output could be  [1, 2, 1, 3, 1, 4, 1, 5, 1]