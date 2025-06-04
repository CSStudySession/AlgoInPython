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
variant1:
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
T(k*m*logk) m是输入行数 , S(k*m) heap和visited最多k个元素 每个元素是长度为m的index list
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

'''
variant2:
given a list of integer arrays. Each array contains positive integers sorted in descending order. 
From each array, select exactly one element to form a combination. Compute the product of the selected elements. 
Your task is to return the k-th largest product among all possible combinations.
Each array may have a different length.
You can assume k is always valid (i.e., not greater than the total number of possible combinations).
Example:
Input:
arrays = [
  [9, 6, 3],
  [8, 4],
  [5, 2]
]
k = 4
Output: 144  # The 4th largest product among all combinations
思路: max-heap + bfs
- 初始状态 每个数组选第一个元素（最大值）形成初始组合索引 把输入看成2d matrix 下标等于行坐标 值等于列坐标 [0, 0, ..., 0]
计算对应乘积，加入 大根堆（用负值模拟最大堆）
用 visited 集合记录访问过的索引组合，避免重复。
- 堆中维护待扩展的组合
每次从堆中弹出当前乘积最大的组合，并从中沿每一维扩展一个新组合 即把其中某一行的索引 +1
如果新组合没有访问过，则计算其乘积并加入堆
重复这个过程 k 次，第 k 次弹出的组合乘积就是答案。

T(k*m*logk) m是输入行数 , S(k*m) heap和visited最多k个元素 每个元素是长度为m的index list
'''
def topKProducts(arrays, k):
    m = len(arrays)
    # 初始索引：[0, 0, ..., 0] 每行取第一个元素
    indices = [0] * m  
    init = 1
    for i in range(m): # initial product
        init *= arrays[i][0]
    
    heap = []
    heappush(heap, (-init, indices))
    visited = set()
    visited.add(tuple(indices))
    
    result = []
    
    while len(result) < k: # 如果k不能保证一定valid 改成while heap and len(ret) < k
        cur, curr_indices = heappop(heap)
        prod = -cur
        result.append(prod)
        for i in range(m): # 遍历每一行 
            if curr_indices[i] + 1 < len(arrays[i]): # 该行还有元素可以尝试
                new_indices = list(curr_indices)
                new_indices[i] += 1
                key = tuple(new_indices)
                if key not in visited:
                    # 更新乘积：先除旧元素，再乘新元素
                    new_prod = prod // arrays[i][curr_indices[i]] * arrays[i][new_indices[i]]
                    heappush(heap, (-new_prod, new_indices))
                    visited.add(key)
    return result

arrays = [
  [9, 6, 3],
  [8, 4],
  [5, 2]
]  # [360, 240, 180, 144, 120]
k = 5

arrays = [
[7,5,3],
[4,2,1]
]   # 
k = 3
print(topKProducts(arrays, k))