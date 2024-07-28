'''

'''

import math
from typing import List

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __lt__(self, other: 'Point'):
        return self.x <= other.x
    
    def generate_points_for_plot(input: List['Point']) -> List['Point']:
        quota = math.ceil(len(input) // 100) # 每个桶点的个数
        cur_cnt = 0 # 当前桶的点个数
        cur_feature_val, cur_label_val = 0.0, 0.0
        ret = []
        for sample in input:
            cur_cnt += 1
            cur_feature_val += sample.x
            cur_label_val += sample.y

            if cur_cnt == quota: # 当前桶满了 该生成plot的点了
                cur_point = Point(cur_feature_val / cur_cnt, cur_label_val / cur_cnt)
                ret.append(cur_point)
                
                # reset all counters
                cur_cnt, cur_feature_val, cur_label_val = 0, 0.0, 0.0
        
        # 因为算quota的时候向上取整过 所以可能还有剩余的点没有处理
        if cur_cnt != 0:
            cur_point = Point(cur_feature_val / cur_cnt, cur_label_val / cur_cnt)
            ret.append(cur_point)

        return ret


            