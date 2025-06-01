from heapq import heappush, heappop
'''
矩阵行列有序 可以二分. 猜一个值mid 然后数矩阵中多少个元素<=mid的方式逐渐二分到答案.
二分范围:matrix[0][0](min value)  matrix[-1][-1](max value)
利用一个helper func每次计算矩阵中<=给定mid的元素个数
 -- 如果该个数<k 说明mid小了 left=mid + 1
 -- 如果个数>=k 说明mid可能是答案 但还可以尝试继续二分更小的 right=mid
T(nlog(max - min)) S(1)
'''
def kthSmallest(matrix: list[list[int]], k: int) -> int:
    if not matrix:
        return -1
    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        cnt = count_num(mid, matrix)
        if cnt >= k:
            right = mid
        else:
            left = mid + 1
    return right

def count_num(mid, matrix):
    i, j = len(matrix) - 1, 0
    cnt = 0
    while i >= 0 and j < len(matrix[0]):
        if matrix[i][j] > mid:
            i -= 1
        else:
            cnt += i + 1
            j += 1
    return cnt


'''
variant:
Given an MxN matrix with its rows sorted in ascending order and an integer k.
Define a sum S which consists of one element from each row.
Find the kth smallest sum S_k.

Example
Input
[
  [1, 3, 5, 7, 9],
  [2, 4, 6, 8, 10]
]
k = 3
Output
5

Explanation
The third smallest sum is returned from this sequence:
1+2, 1+4, 2+3, 1+6, 2+5, 3+4, and so on
思路:利用每行有序的性质 用最小堆 始终扩展当前最小组合 记录访问过的坐标组合 避免重复
- 从每行选第0个元素 即组合索引 [0, 0, ..., 0]
计算起始组合的总和 S = matrix[0][0] + matrix[1][0] + ... + matrix[M-1][0]
将该组合 (sum, indices) 放入最小堆
  - 使用 visited set 记录已访问坐标，避免重复扩展。
- 使用堆进行 BFS 扩展（每次只扩展一个维度）
重复 k 次
 - 弹出堆顶最小元素 (curr_sum, indices)
 - 如果当前是第k个弹出的 直接返回 curr_sum
 - 否则 对于每一行 i 尝试将indices[i]+= 1 来扩展新的组合
如果新组合未访问过 计算其和后加入堆中
T(k*m*logk) m是输入行数 S(k*m)
'''
def kthSmallestSum(matrix, k):
    m, n = len(matrix), len(matrix[0])
    # 初始组合 每一行取第0个元素的组合 [0]*m代表列坐标
    initial = (sum(row[0] for row in matrix), [0] * m)
    heap = [initial]
    visited = set()
    visited.add(tuple(initial[1]))

    for _ in range(k): # 第k次弹出的就是第k小
        curr_sum, indices = heappop(heap)
        for i in range(m): # 遍历每行
            if indices[i] + 1 < n:
                new_indices = list(indices) # 注意要创建新的array 原来的array还在遍历中 别的状态也要用
                new_indices[i] += 1
                if tuple(new_indices) not in visited:
                    # 构造新的组合 sum
                    new_sum = curr_sum - matrix[i][indices[i]] + matrix[i][new_indices[i]]
                    heappush(heap, (new_sum, new_indices))
                    visited.add(tuple(new_indices))
    return curr_sum

matrix = [
  [1, 3, 5, 7, 9],
  [2, 4, 6, 8, 10]
]
k = 3
print(kthSmallestSum(matrix, k))