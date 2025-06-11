'''
在页面上展示pin图片 每个pin有不同的高度 我们要构建一个页面 
使得某一列的pin高度总和正好等于屏幕高度(或最多接近且不超过)
目标是使用最少数量的pin 来“刚好”铺满屏幕的高度
Input:
一个整数max_screen_height 屏幕的总高度
一个整数数组pin_heights:每种pin可用高度(可以无限使用)
Output:一个整数 最少需要的pin数 使得其高度和等于max_screen_height
如果无法组成该高度，返回 -1
Clarifications
每种 pin 数量无限(unlimited supply)
pin高度为正整数 不考虑pin宽度
只能刚好铺满屏幕高度 多余的也不允许
思路:dfs + 记忆化搜索
尝试每种pin的高度, 设当前尝试的为, 当前高度减去h后 递归求解
用memo缓存子问题结果 避免重复计算
H: screen height, N:len(pin_heights)
T(H*N)  S(H) memo + stack
'''
def min_pins_recursive(pin_heights, screen_height, memo):
    if screen_height < 0:
        return -1
    if screen_height == 0:
        return 0
    if memo[screen_height] != None:
        return memo[screen_height]

    res = float('inf')
    for h in pin_heights:
        cur_res = min_pins_recursive(pin_heights, screen_height - h, memo)
        if cur_res != -1:
            res = min(res, cur_res + 1)
    memo[screen_height] = -1 if res == float('inf') else res
    return memo[screen_height]

def min_pins_recursive_wrapper(pin_heights, screen_height):
    memo = [None] * (screen_height + 1)  # -2 表示未计算过
    return min_pins_recursive(pin_heights, screen_height, memo)

'''
解法2: bfs
- 每个状态是一个剩余高度
- 用 BFS 搜索从 screen_height 到 0 的最短路
- 每减一次就是用了一个 pin
H: screen height, N:len(pin_heights)
T(H*N) S(H) for queue and visited
'''
from collections import deque
def min_pins_bfs(pin_heights, screen_height):
    queue = deque([(screen_height, 0)])
    visited = set([screen_height])
    while queue:
        remain_h, count = queue.popleft()
        if remain_h == 0:
            return count
        for h in pin_heights:
            next_h = remain_h - h
            if next_h >= 0 and next_h not in visited:
                visited.add(next_h)
                queue.append((next_h, count + 1))
    return -1  # 无法铺满