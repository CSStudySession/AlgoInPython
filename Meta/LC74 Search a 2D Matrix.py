'''二分搜索
把整个二维矩阵当作一维数组来做 binary search, 下标搜索范围[0, m*n - 1]
pivot_idx = (left + right) // 2
把pivot_idx map back to 2D index, 找到对应的值
pivot_element = matrix[pivot_idx // n][pivot_idx % n]
pivot_idx // n 取行号
pivot_idx % n 取列号
T(m*n) S(1)
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left < right:
        mid = (left + right) // 2
        mid_x, mid_y = mid // n, mid % n
        if matrix[mid_x][mid_y] >= target: # mid可能是答案 drop右边
            right = mid
        else:
           left = mid + 1  # mid不会是答案 drop左边
    if matrix[right // n][right % n] == target: # 有可能不存在 最后要check一下
        return True
    return False



