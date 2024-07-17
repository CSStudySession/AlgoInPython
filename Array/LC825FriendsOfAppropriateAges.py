from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        size = len(ages) # 有多少人
        
        age_num = [0] * 121 # age_num[i]: 第i岁有多少人
        for age in ages:
            age_num[age] += 1
        
        ret = size * size  # 可能的所有请求个数 后面会剔除非法的请求
        for i in range(1, 121):         # 枚举所有可能的年龄(代表某个人)
            for j in range(1, 121):     # 枚举所有可能的年龄(代表某个人)
                if (j <= 0.5 * i + 7) or (j > i):
                    ret -= age_num[i] * age_num[j]
                elif j == i:  # 剔除自己向自己发请求(自环)
                    ret -= age_num[j]
        return ret