
'''
https://leetcode.com/problems/rotate-image/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

x  x  x 
x  x  x
x  x  x
1. 先沿着对角线(左上到右下)翻转
2. 再沿着中轴(竖着的中间轴)翻转
'''
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先沿对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            j, k = 0, n - 1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
        