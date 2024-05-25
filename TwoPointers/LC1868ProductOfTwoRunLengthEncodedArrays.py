from typing import List

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        res = []
        i, j = 0, 0
        cnt1, cnt2 = encoded1[0][1], encoded2[0][1]

        while i < len(encoded1) and j < len(encoded2):
            v1, _ = encoded1[i]
            v2, _ = encoded2[j]
            min_cnt = min(cnt1, cnt2)
            product = v1 * v2

            cnt1 -= min_cnt
            cnt2 -= min_cnt

            if cnt1 == 0:
                i += 1
                if i < len(encoded1):
                    cnt1 = encoded1[i][1]
            if cnt2 == 0:
                j += 1
                if j < len(encoded2):
                    cnt2 = encoded2[j][1]
            
            # 处理res: 如果res[-1]已经有了这个乘积,改变res[-1][1]累加currMin, 没有就append一个新的tuple
            if res and res[-1][0] == product:
                res[-1][1] += min_cnt
            else:
                res.append([product, min_cnt])  
        return res