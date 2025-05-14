'''
思路:把第一行和第一列作为标记空间 记录哪些行列需要清零 可以不使用额外空间完成操作
最后再单独处理第一行和第一列是否需要清零的情况。
T(m*n) S(1)
'''
def setZeroes(matrix: list[list[int]]) -> None:
    row, col  = len(matrix), len(matrix[0])
    first_row_zero = False        
    first_col_zero = False

    # check if the first row contains zero
    for j in range(col):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # check if the first column contains zero
    for i in range(row):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    # use the first row and column as a note
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    # set the marked rows to zero
    for i in range(1, row):
        if matrix[i][0] == 0:
            for j in range(1, col):
                matrix[i][j] = 0

    # set the marked columns to zero
    for j in range(1, col):
        if matrix[0][j] == 0:
            for i in range(1, row):
                matrix[i][j] = 0

    # set the first row to zero if needed
    if first_row_zero:
        for j in range(col):
            matrix[0][j] = 0

    # set the first column to zero if needed
    if first_col_zero:
        for i in range(row):
            matrix[i][0] = 0