'''
研究一组Pins之间的关联关系 每个Pin出现在一个或多个board中 我们希望定义一种关系分数(relation score)来衡量两个Pin的关联程度
关联分数定义：
score = :：两个 Pin 同时出现在同一个 board 中。
score = 2:两个 Pin 不同 board, 但它们各自都和某个中间 Pin 同一个 board。
score = k:定义为两个 Pin 所在 board 图中最短路径的长度。
本质上是 在“Pin-Board-Pin”构建的图上求最短路径。
如果无任何连接，返回 0。
输入：一个 dict,表示 board_name -> list[pins]
操作：
part 1: check_pins_related(pin1, pin2) -> bool
part 2: get_relation_score(pin1, pin2) -> int
part 3: get_all_scores() -> Dict[int, List[Tuple[str, str]]]
返回所有两两Pin对之间的最小关系分组。
Clarification
- Pins和Boards都是字符串且唯一
- 对于多个路径 返回最小 score
- 所有输出结果都fit in memory。
- score为最短路径长度(广度优先搜索 BFS)
- 输出顺序需按score分组
- 不考虑出现 cycle 的样例，但要能处理
思路: 根据输入的board_map 构建图结构 然后在图上做bfs即可
复杂度在每个函数上
'''
from collections import defaultdict, deque

class RelatedPins:
    def __init__(self, board_map):
        self.board_map = board_map
        self.pin_graph = defaultdict(set) # pin graph: pin -> neighboring pins (via common boards)
        self.build_graph()
    # B:# of board, K:# of pins in each board. T(B*k^2) S(E), number of total edges
    def build_graph(self):
        for _, pins in self.board_map.items():
            for i in range(len(pins)): # 构建无向图：连接所有共现的 pin
                for j in range(i + 1, len(pins)):
                    self.pin_graph[pins[i]].add(pins[j])
                    self.pin_graph[pins[j]].add(pins[i])

    # part 1. N:# of pins, E:# of edges. T(N+E) S(N)
    def check_pins_related(self, pin_a, pin_b):
        if pin_a not in self.pin_graph or pin_b not in self.pin_graph:
            return False
        if pin_a == pin_b:
            return True
        # BFS 判断连通性
        visited = set()
        queue = deque([pin_a])
        visited.add(pin_a)
        while queue:
            current = queue.popleft()
            if current == pin_b:
                return True
            for neighbor in self.pin_graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False
    # part 2 N:# of pins, E:# of edges. T(N+E)  S(N)
    def get_relation_score(self, pin_a, pin_b):
        if pin_a not in self.pin_graph or pin_b not in self.pin_graph:
            return 0
        if pin_a == pin_b:
            return 0
        # BFS 计算最短路径
        visited = set([pin_a])
        queue = deque([(pin_a, 0)])  # (pin, current_distance)
        
        while queue:
            current, dist = queue.popleft()
            if current == pin_b:
                return dist
            for neighbor in self.pin_graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return 0  # 不可达

    # part 3.pins两两组合n^2, T(n^2 *(N+E))
    # 优化: Floyd算法 可以优化到 T(N^3)
    def get_all_scores(self):
        all_pins = list(self.pin_graph.keys())
        score_map = defaultdict(list)

        for i in range(len(all_pins)):
            for j in range(i + 1, len(all_pins)):
                pin1 = all_pins[i]
                pin2 = all_pins[j]
                score = self.get_relation_score(pin1, pin2)
                if score > 0:
                    score_map[score].append((pin1, pin2))
        return score_map