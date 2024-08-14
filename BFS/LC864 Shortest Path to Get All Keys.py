'''
https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
You are given an m x n grid grid where:
'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions.
You cannot walk outside the grid, or walk into a wall.
If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. 
This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 3:
Input: grid = ["@Aa"]
Output: -1

思路 BFS
1.初始化：首先，找到起点 '@' 的位置，并将其加入队列 queue 中，初始时未获得任何钥匙。
使用一个位掩码 key 来记录所有钥匙的总数，然后计算出当所有钥匙都被收集时的目标状态 goal。
2.BFS遍历 在每一轮BFS中 从队列中取出当前的位置、当前收集到的钥匙状态和当前步数。
对当前点的四个方向进行扩展：
- 如果是墙 '#'，跳过。
- 如果是钥匙（小写字母），更新钥匙的状态。
- 如果是锁（大写字母），检查是否有对应的钥匙，有则继续，否则跳过。
- 对于空地 '.'，直接继续搜索。
- 每走一步后，将新状态加入队列，并将状态标记为已访问。

3.终止条件 一旦达到目标状态（所有钥匙都被收集），返回当前步数。如果队列为空但仍未达到目标状态，返回 -1 表示无法收集所有钥匙。

时间复杂度分析
状态数：由于有 k 把钥匙，钥匙的状态可以用 2^k 表示，而每个位置 (i, j) 可能有 2^k 种状态。
BFS遍历 队列中最多会有 O(m * n * 2^k) 个状态，每个状态最多有 4 个扩展方向。
因此，时间复杂度为 O(m * n * 2^k * 4)，即 O(m * n * 2^k)。

空间复杂度分析
队列空间：最多会有 O(m * n * 2^k) 个状态在队列中。
访问标记：同样需要 O(m * n * 2^k) 的空间来存储访问过的状态。
因此，空间复杂度也是 O(m * n * 2^k)
'''
from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row, col, key = len(grid), len(grid[0]), 0
        queue = deque()
        visited = set()
        # 遍历grid 寻找起点和收集所有钥匙数
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '@': # 起点
                    queue.append((i, j, 0, 0))
                    visited.add((i, j, 0))
                elif grid[i][j].isalpha() and grid[i][j].islower(): # 钥匙
                    key += 1
        goal = (1 << key) - 1
        
        # BFS中的offset
        dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
        while queue:
            cur_x, cur_y, cur_key, cur_dist = queue.popleft()
            if cur_key == goal:
                return cur_dist
            
            for i in range(4):
                x, y = cur_x + dx[i], cur_y + dy[i]
                if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == '#':
                    continue
                char = grid[x][y]
                if char >= 'a' and char <= 'z':
                    nxt_key = cur_key | 1 << (ord(char) - ord('a'))
                    if (x, y, nxt_key) not in visited:
                        queue.append((x, y, nxt_key, cur_dist + 1))
                        visited.add((x, y, nxt_key))
                elif char >= 'A' and char <= 'Z':
                    pos = ord(char) - ord('A')
                    if (cur_key >> pos) & 1 and (x, y, cur_key) not in visited:
                        queue.append((x, y, cur_key, cur_dist + 1))
                        visited.add((x, y, cur_key))
                else:
                    if (x, y, cur_key) not in visited:
                        visited.add((x, y, cur_key))
                        queue.append((x, y, cur_key, cur_dist + 1))
        
        return -1
    
'''
注意 如果钥匙表示不连续，意味着不能简单地用 ord(char) - ord('a') 来计算位掩码，因为每个钥匙的索引值可能不再是连续的。
为了解决这个问题，可以使用一个映射（哈希表）来将每个钥匙字符映射到一个特定的位位置，从而正确处理不连续的钥匙。
逻辑如下:
elif grid[i][j].isalpha() and grid[i][j].islower():  # 钥匙
    if grid[i][j] not in key_map:
        key_map[grid[i][j]] = key_index
        key_index += 1
goal = (1 << key_index) - 1
nxt_key = cur_key | (1 << key_map[char])
if char.lower() in key_map and (cur_key >> key_map[char.lower()]) & 1
'''