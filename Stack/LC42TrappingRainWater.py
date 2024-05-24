from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        ret = 0

        for i in range(len(height)):
            while stk and height[stk[-1]] <= height[i]:
                top = stk[-1]
                stk.pop()
                
                if not stk:
                    break
                
                ret += (i - stk[-1] - 1) * (min(height[i], height[stk[-1]]) - height[top])
            
            stk.append(i)
            
        return ret