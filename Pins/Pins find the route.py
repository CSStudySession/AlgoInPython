'''
给定一组 [origin, destination] 形式的机票 乱序, 你需要找出一条唯一的完整行程路线
每张票只能从出发城市直达目的城市
所有城市都是大小写字母组成 可以是完整城市名 也可以是字符
所有票拼成的一条路径是连通的 起点唯一 终点唯一
输入:一个 List[List[str]] 形式的机票列表，每张票是 [from, to]
输出:一个 List[str] 表示完整行程路径，按顺序排列的城市列表。
Clarification
初始问题中 假设输入始终合法 存在且仅存在一条唯一路径
follow-up 才考虑 corner cases:
多起点 / 多终点 / 环路 / 断裂路线 / 没有起点城市等
'''
'''
思路:构建哈希映射 + 找起点顺序连接（题干默认唯一路径）
记录 from_city -> to_city 的映射
记录所有的目的地(to_set) 从所有起点中找出不在to_set中的起点(即唯一起点)
从起点出发依次查映射构建路径
T(n) S(n)
'''
def build_route(tickets):
    # 构建出发->到达 mapping
    route_map = {}
    to_set = set()

    for src, dst in tickets:
        route_map[src] = dst
        to_set.add(dst)

    # 找起点: 起点不在to_set中(第一问假设起点存在且唯一)
    start = None
    for city in route_map:
        if city not in to_set:
            start = city
            break # 起点唯一 找到就break

    # 从起点出发逐个构建完整路径
    res = [start]
    while start in route_map:
        start = route_map[start]
        res.append(start)

    return res

'''
followup1:在原始解法基础上对以下corner cases加入异常判断&异常抛出:
- 没有起始城市（起点在所有终点集合中找不到）
- 存在环(如:A->B, B->C, C->A)
- 多个起点(多条链)
- 多个终点（有多余的目的地）
- 路线不连通(多个disconnected component)
'''
from collections import defaultdict
def build_route_with_checks(tickets):
    route_map = {}
    to_set = set()
    from_set = set()
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    # 构建图、统计出度/入度
    for src, dst in tickets:
        if src in route_map:
            raise ValueError(f"Multiple flights from same origin: {src}")
        route_map[src] = dst
        from_set.add(src)
        to_set.add(dst)
        out_degree[src] += 1
        in_degree[dst] += 1

    # 1. 找起点：from_set 中不在 to_set 的城市
    possible_starts = [city for city in from_set if city not in to_set]
    if len(possible_starts) == 0:
        raise ValueError("No valid start city found (cycle or all cities are destinations).")
    if len(possible_starts) > 1:
        raise ValueError("Multiple starting cities found.")
    
    start = possible_starts[0]

    # 2. 检查终点唯一性
    all_cities = from_set | to_set
    possible_ends = [city for city in all_cities if city not in from_set]
    if len(possible_ends) == 0:
        raise ValueError("No valid destination city found (cycle detected).")
    if len(possible_ends) > 1:
        raise ValueError("Multiple destination cities found.")

    # 3. 构建路径
    route = [start]
    visited = set()
    while start in route_map:
        visited.add(start)
        start = route_map[start]
        if start in visited:
            raise ValueError("Cycle detected in route.")
        route.append(start)

    # 4. 判断是否完整使用所有票
    if len(route) != len(tickets) + 1:
        raise ValueError("Route is disconnected or broken.")

    return route

'''
followup2: 题目输入改为可能含环. 输入依然合法, 使用所有票并输出一条字典序最小的路径, 起点已给定
思路: 由于字典序要求 先对tickets倒序排序
遍历时从字典序最小的城市出发(reverse + pop保证)
T(nlogn + n)  S(n)
'''
import collections
def find_route_lexical(tickets, start_city):
    # 按字典序逆序排序 便于pop出最小目的地
    tickets.sort(reverse=True)
    graph = collections.defaultdict(list)
    
    # 构建图：起点 -> list[终点]（按字典序倒序）
    for src, dst in tickets:
        graph[src].append(dst)
    res = []
    
    def dfs(city): # 当前city没有out edges了:graph[city]为空 才把它加入结果集
        while graph[city]:
            next_city = graph[city].pop()
            dfs(next_city)
        res.append(city)  # 后序遍历回溯加入路径

    dfs(start_city)
    return res[::-1]