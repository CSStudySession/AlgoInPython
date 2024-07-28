'''
Time complexity : O(max(N,M)), where N and M are the lengths of the input strings respectively. It's a one-pass solution.

Space complexity : O(max(N,M)).

Despite the fact that we did not keep arrays of revision numbers, 
we still need some additional space to store a substring of the input string for integer conversion.

In the worst case, the substring could be of the original string as well.
'''
from typing import List

class Solution:
    def get_chunk(self, version: str, n: int, p: int) -> List[int]:
        # 已经走完了当前str
        if p > n - 1:
            return 0, p

        # 找一下个"."的位置
        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1 # p_end最后停在.的idx

        # 截取出对应的数字 p_n在str结尾处需要特判
        num = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])
        # p指向下一个chuck的起点 为了下一次截取数字
        p = p_end + 1
        return num, p

    def compareVersion(self, version1: str, version2: str) -> int:
        p1, p2 = 0, 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2: # 注意这里是or 有一个str还有就接着走
            num1, p1 = self.get_chunk(version1, n1, p1)
            num2, p2 = self.get_chunk(version2, n2, p2)
            if num1 != num2:
                return 1 if num1 > num2 else -1

        # 走过一遍都没return 两个版本最后相等
        return 0   