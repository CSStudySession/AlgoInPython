from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        stk = []
        heights.append(-1)

        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                top = stk.pop()
                if not stk:
                    ret = max(ret, heights[top] * i)
                else:
                    ret = max(ret, heights[top] * (i - stk[-1] - 1))
            stk.append(i)        
        
        return ret