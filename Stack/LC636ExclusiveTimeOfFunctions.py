from typing import List
# stack装ID:还没有end的logId. 
# 每碰到start就push 并更新stack[-1]的结果.碰到end就stack.pop()并计算结果. 
# ret array记录每个id的时长
def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    ret = [0] * n
    stack = []
    prev_ts = 0
    for i in range(len(logs)):
        log_strs = logs[i].split(':')
        id, op, ts = int(log_strs[0]), log_strs[1], int(log_strs[2])
        if op == 'start':
            if stack:
                pre_id = stack[-1]
                ret[pre_id] += ts - prev_ts
            stack.append(id)
            prev_ts = ts
        else:
            prev_id = stack.pop()
            ret[prev_id] += ts - prev_ts + 1 # 注意要+1
            prev_ts = ts + 1 # 注意要+1
    return ret