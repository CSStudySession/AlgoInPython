from typing import List

class Solution:
    # method 1: space o(1) compare: matrix[i][j] != matrix[i-1][j-1]
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
     
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True