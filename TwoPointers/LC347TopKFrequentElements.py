import collections
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        self.counter = collections.Counter(nums)
        keys = list(self.counter.keys())
        idx = self.partition(keys, k, 0, len(keys)-1)
        return keys[:idx+1]
    
    def partition(self, keys, k, start, end) -> int:
        if start >= end:                                # corner case: keys is empty. start = 0, end = -1
            return start
        left, right = start - 1, end + 1
        
        pivot = self.counter[keys[(left + right) // 2]]
        while left < right:
            while True:
                left += 1
                if self.counter[keys[left]] <= pivot:
                    break
            while True:
                right  -= 1
                if self.counter[keys[right]] >= pivot:
                    break
            if left < right:
                keys[left], keys[right] = keys[right], keys[left]
        if k <= right - start + 1:
            return self.partition(keys, k, start, right)
        else:
            return self.partition(keys, k - (right - start + 1), right + 1, end)