'''
https://leetcode.com/problems/shortest-distance-from-all-buildings/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

'''

from typing import List
from collections import defaultdict

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist, k = defaultdict(int), 0
