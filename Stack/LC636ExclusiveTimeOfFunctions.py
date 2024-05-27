from typing import List

class Solution:
    # stack装ID: 还没有end的logId. 每碰到start就push+结算stack[-1]的结果, 碰到end就stack.pop()+计算结果. 
    # res array记录每个id的时长
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ret = [0] * n
        stack = [] # methods being executed
        prev_ts = 0
        for log in logs: 
            log_str = log.split(":")
            id, op, ts = int(log_str[0]), log_str[1], int(log_str[2])
            if op == "start": # calculate previous total, then push newId into stack
                if stack:
                    prev_id = stack[-1]
                    ret[prev_id] += ts - prev_ts
                stack.append(id)
                prev_ts = ts
            else:
                ret[stack[-1]] += ts - prev_ts + 1 # note +1 here
                stack.pop()
                prev_ts = ts + 1 # note +1 here
        return ret