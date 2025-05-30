''' similar question: 1424. Diagonal Traverse II 
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

'''
variant1: given a full matrix, and you had to print out the anti-diagonal order?
思路: 找规律 一共m+n-1条对角线 每次循环打印一条 设当前是第k条:
1. k<n: 起点的行坐标i总为0, j即为k
2. k>=n:起点的列坐标j总为n-1(最后一列) 因为i+j==k 所以i=k-n+1
T(n) S(1)
'''
def findDiagonalOrder(self, nums: list[list[int]]) -> None:
    m, n = len(nums), len(nums[0])
    
    for k in range(m + n - 1):
        if k < n: # 行坐标是0
            i, j = 0, k
        else:     # 列坐标是n-1
            i, j = k - n + 1, n - 1 # i+j==k
        while i < m and j >= 0: # i,j不越界
            print(nums[i][j], " ")
            i += 1
            j -= 1
        print("\n")

# nums = [[1,2,3], [4,5,6,],[7,8,9]]
# print(anti_diagonal_traversal(nums))