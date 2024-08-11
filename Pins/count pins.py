'''
https://leetcode.com/discuss/interview-question/4245529/Pinterest-or-Phone-or-Count-Pins

Pinterest app screen is two columns of images (pins).
Each pin has a top and bottom index (top < bottom), and has a column represented by "L" or "R".
Given an unsorted list of non-overlapping pins like

pins = [(top_ind,bottom_ind,column),...,]
and a screen_length of screen_len
Return the maximum number of pins the user can possibly see (fully).
That is, complete this:

def get_max_pins(pins,screen_len):
    max_pins = 0
	...
    return max_pins
Example:

input:
  pins = [(1,4,"L"),(2,3,"R"),(4,8,"R"),(6,9,"L")] 
  screen_len = 5
output: 2


思路:
将pins按照结束位置bottom_ind排序。这样可以按顺序处理pins 确保我们总是处理当前结束位置最靠前的pin。
使用一个最小堆fitted_pins_heap 来存储当前可见的pins。堆中的元素按开始位置top_ind排序。

遍历排序后的pins:
计算当前pin结束位置对应的屏幕起始位置s_start
如果当前pin的开始位置大于或等于s_start 说明这个pin可以完全显示在屏幕上 将其加入堆中。
检查堆顶的pin 即开始位置最小的pin 是否仍然可见。如果不可见，就将其从堆中移除。
动态更新最大可见pins数量。

时间复杂度分析：
对pins进行排序 O(n log n) 其中n是pins的数量。
遍历排序后的pins O(n)
对于每个pin 可能需要进行堆操作：
插入操作 O(log n)
删除操作 最坏情况下可能需要删除所有之前插入的pins 总复杂度为O(n log n)
总的时间复杂度 O(n log n)

空间复杂度分析：
排序后的pins列表 O(n)
最小堆fitted_pins_heap 最坏情况下可能包含所有pins 因此空间复杂度为O(n)
总的空间复杂度 O(n)
'''

import heapq

def get_max_pins(pins, screen_len):
	if not screen_len or not pins:
		return 0
	# Sort pins based on their end position
	pins = sorted(pins, key = lambda x: x[1])
	fitted_pins_heap = []      # Create this heap, to push out the pin with smallest start position
	max_pins = 0
	for idx in range(len(pins)):
		s_start = pins[idx][1] - screen_len    # 当前pin如果贴着屏幕下断点展示 屏幕的起点坐标是s_start
		# Add current pin to fitted
		if pins[idx][0] >= s_start:            # 当前pin的起点坐标 不能比s_start还小(还小说明给定的屏幕尺寸放不下该pin)       
			heapq.heappush(fitted_pins_heap, pins[idx])   # 能放下该pin 就入堆 堆中元素按照pin top index从小到大排序
		# Push out pins that does not fit any more with the new end position
		while fitted_pins_heap and fitted_pins_heap[0][0] < s_start:  # 堆顶元素的起点如果小于s_start 说明屏幕框不住堆顶的pin了
			heapq.heappop(fitted_pins_heap)
		max_pins = max(max_pins, len(fitted_pins_heap))
	return max_pins

# unit test
pins = [(1,4,"L"),(2,3,"R"),(4,8,"R"),(6,9,"L")]
screen_len = 5
print(get_max_pins(pins, screen_len))