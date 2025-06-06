from collections import defaultdict
'''
Given a set of points on a 2D plane, find all combinations of points that can form a rectangle.
思路：一个矩形的两个对角线 长度相等 交点相同（即中点一致）
因此 枚举任意两个点作为对角线的两个端点 (p1, p2) 记录：
- 对角线的中点坐标
- 对角线的平方长度
把所有具有相同中点 & 相同长度的点对归为一组
每一组中 两两组合点对 可以组成一个矩形 4个点正好为两个对角线端点
注意去掉重复的四个点的组合: sort一下放set中
T(n^4) 最差情况下 所有point pair都有相同的key 这样n^2个pairs 能组成n^4个矩形 -> S(n^4) 
'''
def find_all_unique_rectangles(points):
    n = len(points)
    point_pairs = defaultdict(list)
    # 枚举所有点对 按（中点，长度）分组
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            mid_x = x1 + x2
            mid_y = y1 + y2
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
            key = (mid_x, mid_y, dist_sq)
            point_pairs[key].append(((x1, y1), (x2, y2)))
    rectangle_set = set()
    result = []
    # 枚举每组中所有点对组合
    for pair_list in point_pairs.values():
        for i in range(len(pair_list)):
            for j in range(i + 1, len(pair_list)):
                p1, p2 = pair_list[i]
                p3, p4 = pair_list[j]
                rect = tuple(sorted([p1, p2, p3, p4])) # 为了去重
                if rect not in rectangle_set:
                    rectangle_set.add(rect)
                    result.append(list(rect))
    return result