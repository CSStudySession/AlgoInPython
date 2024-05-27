from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals = sorted(intervals) # sorted on first element of inner list
        cur_left, cur_right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur_right:
                ret.append([cur_left, cur_right])
                cur_left, cur_right = intervals[i][0], intervals[i][1]
            else:
                cur_right = max(cur_right, intervals[i][1])
        ret.append([cur_left, cur_right]) # last interval needs to process outside of for loop
        return ret