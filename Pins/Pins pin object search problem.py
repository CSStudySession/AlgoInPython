'''
给定一个Pinterest的pin图像 由一个二维像素数组组成. 图像中包含若干“物体” 每个物体由相连的像素构成.
目标:统计pin中的物体数量
定义：
- isSameObject(p1, p2) 是系统提供的黑盒函数 用于判断两个像素是否属于同一个物体
- 只有两个或更多相连像素才能构成一个“物体”
- 像素相连仅限上下左右四个方向
输入: Pixel[][] pin: 一个二维数组，表示图像上的像素点
输出:一个int值 代表pin图像中的物体数量
Clarification
- 物体是否可以重叠？ 不可以（简化假设）
- 物体是否是连通的？ 是的
- 如果两个像素都不属于任何物体 isSameObject 返回什么？ 返回 False
- 是否允许只有一个像素构成物体？ 不允许（至少两个像素）
思路:BFS
遍历pin grid, 没有visited的话 进行bfs. 注意bfs过程中 需要判断是否有两个或以上的"same pixel"
T(m*n) S(m*n)
'''
from collections import deque

def is_same_object(p, q) -> bool:
    pass

def count_obj(pin):
    rows, cols = len(pin), len(pin[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    obj_cnt = 0
    # bfs helper function
    def bfs(start_r, start_c):
        queue = deque()
        queue.append((start_r, start_c))
        visited[start_r][start_c] = True
        valid_obj = False # 找到2个或以上才能算valid
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            i, j = queue.popleft()
            for di, dj in dirs:  # 上下左右四邻
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                    # 判断是否同一个object
                    if is_same_object(pin[ni][nj], pin[i][j]):
                        visited[ni][nj] = True
                        queue.append((ni, nj))
                        valid_obj = True
        return valid_obj

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if bfs(i, j):  # 至少连着两个 pixel 才算一个 object
                    obj_cnt += 1
    return obj_cnt

'''
Follow-up Questions / Variations
- 如果图太大，不能在单机内完成怎么办？
系统设计层面考察：分布式处理大图像的方法。
  - 方式一（图块切分 + MapReduce 处理）：
把图像等分成多个子图，每个子图单独统计局部物体
对于贴边的物体，需要保留至少一个边界像素用于跨子图合并
 - 通常会将 边缘上的像素或其连通组 单独输出给 reducer
 - 例如对tile上的一对相邻边界pixel (p1, p2) 它们属于不同tiles 但isSameObject(p1, p2) 返回 true
   则输出一个 key 比如object_candidate_group_id = hash(p1, p2)
- 这对信息通过shuffle被发送到reducer 负责合并重复计数
Reducer 阶段合并物体
  - 对reducer收到的边界对象进行聚合(如并查集 union) 将跨tile的多段物体合并为一个物体
  - 邻接子图的边界数据需要发送到同一个计算节点 以保证物体不会被重复计算
  - 方式二（自中心扩张法）：
从中心开始处理，先合并中心区域的子图
再向四周扩展，边处理边合并已知信息
更类似 增量构建 或 “区域生长”法
'''