from typing import List
import collections, random

class Solution:
    def __init__(self, nums: List[int]):
        self.dict = collections.defaultdict(list) # dict: {val: [idex0, idx1, ...]}
        for i in range(len(nums)):
            self.dict[nums[i]].append(i)      

    def pick(self, target: int) -> int:
        indexList = self.dict[target]
        return random.choice(indexList) # Return a random element from the non-empty indexList. If indexList is empty, raises IndexError.
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)