# stack装ID:还没有end的logId. 维护一个变量prev_ts来计算时间 
# 每碰到start 先更新stack[-1]的结果 再把start对应的id push stack, 并更新prev_ts. 
# 碰到end就stack.pop()并计算结果 注意有off by one issue. 
# ret array记录每个id的时长
def exclusiveTime(n: int, logs: list[str]) -> list[int]:
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