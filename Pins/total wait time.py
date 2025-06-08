'''
lc link: https://leetcode.com/discuss/interview-question/1920662/google-phone-calculate-total-wait-time

Calculate the total wait time for a customer C to speak to an agent given N agents, M customers, 
and T[] time for an agent to serve a customer. 
T[i] represents the amount of time it takes for an agent i to serve one customer. 
One agent can serve one customer at a time. All N agents can serve concurrently. 
The customer chooses the agent with the lowest wait time.

Examples:
N = 2
M = 2
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Customer C will wait 4 minutes.

N = 2
M = 4
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Third customer chooses agent 1. Forth customer chooses agent 2.
Customer C will wait 8 minutes.

Initial questions:
Bounds on N and M - No bounds
Can N or M be zero - Both can be zero
Are the T values constant - Yes
Are the T values integers - Yes

time: O(n + m*lg(n))
space: O(n)
'''
from typing import List
from collections import defaultdict
import heapq

# N: agent number  M: customer number
def wait_time(N:int, M:int, T:List[int]) -> int:
    if M < N:     # agent number > customer number: no need to wait
        return 0
    
    # 让所有agents 先把能接的customers都接上 也就是N个customers 
    # (time,idx)代表:idx号的agent接待下一个customer 需要等待的时间为time
    agent_status = [(time, idx) for idx, time in enumerate(T)]
    heapq.heapify(agent_status)

    # 处理剩下的(M-N)个customers
    remain = M - N
    while remain:
        time, idx = heapq.heappop(agent_status)
        heapq.heappush(agent_status, (time + T[idx], idx))
        remain -= 1

    # the next available agent would be the top of the heap
    # the waiting time is the first element of (time, idx)
    # if agent id is required, it's agent_status[0][1]
    return agent_status[0][0]

N = 2
M = 8
T = [4, 5]

print(wait_time(N, M, T))

'''
followup:
what if client number is far greater than agent number? (M >> N)
what if there's a constraint on time[i] that 1 <= time[i] <= 10, 
how would you use this to your advantage?

思路:
let's assume we only use the fastest agent to work with all clients, 
it'll take min(time[i]) * m time to finish m client: we can consider it as upper bound.
we could only get faster when we use more agents, so we can do a binary search between [0, min(time[i]) * m],
to find the smallest timestamp that is possible to finish (m - n + 1) clients.

-- 为何最少要处理完(m-n+1)个clients?
想象一下 什么情况下 新的client C才能被处理? 一定是最后剩下了(n - 1)个clients由(n-1)个agents处理 
这样剩下1个agent空出来给这个client C. 所以处理完的clients数 = m - (n - 1) = m - n + 1个 

At each timestamp x, agent i can at most finish Math.floor(x / time[i]) clients, 
so to check if it's possible for timestamp x to finish w clients, 
just sum all (x / times[i]) for all agents and check if it's >= w.
'''

def total_wait_time(n:int, m:int, times:List[int]):
    # there are more number of agents than customers
    if n > m:
        return 0

    # Calculating the minimum and maximum service times from the given times
    min_time, max_time = 0, min(times)

    # Wait time will be in this range because in the worst case
    # there will be only one agent with max_time and the customer
    # needs to wait for them
    low, high = min_time, m * max_time
    freq_map = defaultdict(int)
    # 针对(1 <= time[i] <= 10)这一特点的优化 这个条件使得map里的key数量不会超过10个
    for t in times:          # key: serving时长t, val: 对应的agent个数
        freq_map[t] += 1

    while low < high:
        mid = low + (high - low) // 2
        # Compute the total number of customers that can be served
        # within 'mid' amount of time by counting how many times each
        # agent can serve a customer
        sum_customers_served = sum(mid // time * freq_map[time] for time in freq_map)

        if sum_customers_served >= m - n + 1:
            high = mid
        else:
            low = mid + 1

    return low

# Time complexity: approximately O(N + log(m * max_time))
# as we have a freq map it will reduce the sum time to O(1)
# Space complexity: O(1) -- only 10 possible values for time[i]

# Example usage:
times = [4, 5]  # each agent's service time
n = 2  # number of agents
m = 8  # number of customers
print(total_wait_time(n, m, times))

'''
followup: 二分后 如果要求which agent id serve?
Binary Search 的版本是先找出 Julie 等待的最短时间 T 
然后需要在这个时间点看 哪个 agent 刚好变空闲并服务.
思路:找到 T 之后 遍历所有agent 判断：
在T - 1时间内 每个 agent 已经服务了多少人
在恰好时间 T 时，有哪些 agent 会空闲: T % time[i] == 0
Julie 会被其中编号最小的那一个 agent 服务
在上面的followup code后面 加下面的代码段即可:

    # 找到在 wait_time 时变空闲的 agent
    served_before = 0
    for time in times:
        served_before += (wait_time - 1) // time
    k = m - served_before - 1  # Julie 是第 k 个在 wait_time 时间被服务的人
    for idx, t in enumerate(times):
        if wait_time % t == 0:
            if k == 0:
                return wait_time, idx  # 找到为 Julie 服务的 agent
            k -= 1
    return wait_time, -1  # 不应该走到这里
'''