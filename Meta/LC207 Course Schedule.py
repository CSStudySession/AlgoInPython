#TODO: return a list of course
import collections
# 拓扑排序 T(N + E)  S(N)
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    in_degree = [0] * numCourses # 记录每个节点的入度
    graph = collections.defaultdict(list) # 邻接表表示图
    for pair in prerequisites: # 初始化图和入度数组
        graph[pair[1]].append(pair[0])
        in_degree[pair[0]] += 1
    queue = collections.deque()
    for i in range(len(in_degree)):
        if in_degree[i] == 0: # 入度为0的点入队
            queue.append(i)
    cnt = 0 # 记录结果集中 点的个数
    while queue:
        cur = queue.popleft()
        cnt += 1 # 当前出队的点 一定是入度为0的点
        for nbr in graph[cur]: # 遍历邻居 入度-1 检查是否可以入队
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    return cnt == numCourses