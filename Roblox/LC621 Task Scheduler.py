'''
1.统计每个任务出现频率 因为频率最高任务决定了任务调度框架
2.计算时间框架
 -- 假设出现频率最高的任务有max_count次 则可以将它们分成max_count-1个间隔 
    每个间隔长度为n+1 (包含一个当前任务和n个间隔或其他任务
 -- 初步时间 = (max_count - 1) * (n + 1)
 -- 考虑多个任务拥有相同最大频率情况:需要在最后一个间隔中放入这些相同频率的任务->加上这些任务的个数
3.特殊情况:当n=0或者任务数量本身就很多时 调度时间不会被间隔限制 此时结果是任务总数len(tasks)
T(n) S(1)
'''
def leastInterval(tasks: list[str], n: int) -> int:

    freq = [0] * 26 # freq of tasks. 任务都是大写字母表示 可以转化为数组下标
    max_count = 0
    for task in tasks: # count freq of each task
        freq[ord(task) - ord('A')] += 1
        max_count = max(max_count, freq[ord(task) - ord('A')]) # find max freq
    # 根据greedy 每个max_cnt的元素需要单独一组 中间塞其他的
    time = (max_count - 1) * (n + 1) # 每组n+1个时间片
    for f in freq:         # 计算有多少个任务都是max_cnt个
        if f == max_count:
            time += 1      # 最后一组不需要idle直接排在一块  
    # n==0时 greedy失败 此时需要len(tasks)时间完成所有任务
    return max(len(tasks), time)
