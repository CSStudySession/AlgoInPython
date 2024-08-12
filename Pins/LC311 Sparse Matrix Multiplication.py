'''
https://leetcode.com/problems/sparse-matrix-multiplication/description/

Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. 
You may assume that multiplication is always possible.

Example 1:
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]

Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]

思路:直接按照定义三重循环算. 注意利用稀疏矩阵的特性 mat1[i][j] mat2[j][k]先判断是否为0再进行后续逻辑运算
时间: O(row_1*row_2*col_2)
空间: O(1)
'''
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not len(mat1) or not len(mat2):
            return [[]]
        
        row_1, row_2, col_2 = len(mat1), len(mat2), len(mat2[0])
        ret = [[0 for _ in range(col_2)] for _ in range(row_1)] # 矩阵乘完之后的结果: row_1行 col_2列

        for i in range(row_1):
            for j in range(row_2):
                if mat1[i][j] == 0:     # 稀疏矩阵的优化: 0多 遇到0就跳过
                    continue 
                for k in range(col_2):
                    if mat2[j][k] == 0: # 稀疏矩阵的优化: 0多 遇到0就跳过
                        continue
                    # res[i][k] = Aij_0 * Bj_0k + Aij_1 * Bj_1k + Aij_2 * Bj_2k + ...
                    # res[0][0] = A00 * B00 + A01 * B10 + A02 * B20
                    # i和k始终是0, j不停的变换0，1，2....
                    ret[i][k] += mat1[i][j] * mat2[j][k]  # 注意这里是+=
        return ret