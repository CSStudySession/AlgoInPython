from collections import defaultdict, deque
# 拓扑排序 T(N + E)  S(N)
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    in_degree = [0] * numCourses # 记录每个节点的入度
    graph = defaultdict(list) # 邻接表表示图
    for pair in prerequisites: # 初始化图和入度数组
        graph[pair[1]].append(pair[0])
        in_degree[pair[0]] += 1
    queue = deque()
    for i in range(len(in_degree)):
        if in_degree[i] == 0: # 入度为0的点入队
            queue.append(i)
    cnt = 0 # 记录结果集中 点的个数
    # ret = []
    while queue:
        cur = queue.popleft()
        cnt += 1 # 当前出队的点 一定是入度为0的点
        # ret.append(cur)
        for nbr in graph[cur]: # 遍历邻居 入度-1 检查是否可以入队
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    return cnt == numCourses
    # return ret if cnt == numCourses else []

'''
followup:DFS可以解吗?(不要求code) -> 可以 算法流程如下
将课程依赖关系建成邻接表（图）
对每个课程进行DFS 判断是否存在环
使用 visited 数组进行标记，避免重复访问
 - 0: 没访问
 - 1: 正在访问中（即当前递归栈上的节点）
 - 2: 已访问完毕的节点
如果在 DFS 中再次访问到“正在访问中”的节点，说明图中有环，不能完成所有课程。
'''
def canFinish_dfs(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # 建图：key 是前置课程，value 是它所指向的课程（即后续要学的课程）
    graph = defaultdict(list)
    for cur, pre in prerequisites:
        graph[pre].append(cur)

    # visited 状态：0=未访问，1=正在访问，2=已访问完成
    visited = [0] * numCourses

    def dfs(course: int) -> bool:
        if visited[course] == 1:
            # 当前节点正在访问中，又被访问 -> 有环
            return False
        if visited[course] == 2:
            # 当前节点已经访问完成 -> 无需再DFS
            return True
        # 标记为正在访问
        visited[course] = 1
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False
        # 访问完成，标记为 2
        visited[course] = 2
        return True
    # 对每个课程都跑一遍 DFS（有可能是多个连通图）
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True