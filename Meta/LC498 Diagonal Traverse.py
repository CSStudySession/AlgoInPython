'''
找规律 1.一共m+n-1条对角线. 2.方向不考虑 第k条对角线起始点(i,j):
- k < n: (0, n)  k >= n: (k - n + 1 , n - 1)
3.考虑方向 k%2==0时 reverse对角线遍历顺序
T(m*n) S(1) 
'''
def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
    ret = []
    m, n = len(mat), len(mat[0])
    
    for k in range(m + n - 1):
        level = [] # 当前对角线
        if k < n: # 行坐标是0
            i, j = 0, k
        else:     # 列坐标是n-1
            i, j = k - n + 1, n - 1 # i+j==k
        while i < m and j >= 0: # i,j不越界
            level.append(mat[i][j])
            i += 1
            j -= 1
        if k % 2 == 0: # 偶数行翻转
            level.reverse() # reverse() in-place op.
        ret.extend(level) # extend() in place modify origin list
    return ret