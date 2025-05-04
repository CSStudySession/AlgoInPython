'''
矩阵行列有序 可以二分. 猜一个值mid 然后数矩阵中多少个元素<=mid的方式逐渐二分到答案.
二分范围:matrix[0][0](min value)  matrix[-1][-1](max value)
利用一个helper func每次计算矩阵中<=给定mid的元素个数
 -- 如果该个数<k 说明mid小了 left=mid + 1
 -- 如果个数>=k 说明mid可能是答案 但还可以尝试继续二分更小的 right=mid
T(nlog(max - min)) S(1)
'''

def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
    if not matrix:
        return -1
    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        cnt = self.count_num(mid, matrix)
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return right

def count_num(self, mid, matrix):
    i, j = len(matrix) - 1, 0
    cnt = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > mid:
            i -= 1
        else:
            cnt += i + 1
            j += 1
    return cnt