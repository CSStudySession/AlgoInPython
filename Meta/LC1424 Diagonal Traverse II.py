import collections
'''
每次输出的方向 都是从左下角到右上角.注意输入矩阵可能不完整!
思路:bfs + 找规律. 把矩阵向右旋转45度 画图看更清晰 按题意输出是一个标准的bfs序
对当前出队元素 两个规律: 
1.只要在第一列(j==0) 下一行元素如果有 就入队 2.若下一列元素存在(j+1<当前list size) 就入队
T(N) S(sqrt(N)) 对角线元素个数之和为N:1+2+..+k==n -> k=O(sqrt(N)) 队列中最多有k个元素
'''
def findDiagonalOrder(nums: list[list[int]]) -> list[int]:
    ret = []
    if not nums:
        return ret
    queue = collections.deque([(0,0)])
    while queue:
        i, j = queue.popleft()
        ret.append(nums[i][j])
        if j == 0 and i + 1 < len(nums):
            queue.append((i + 1, j))
        if j + 1 < len(nums[i]):
            queue.append((i, j + 1))
    return ret

'''
variant1: anti-diagonal traversal and return a list of list by levels. 从右上到左下
注意matrix可能不完整!不是m*n都有数字
思路: bfs 列优先. 画图看 把矩阵顺时针旋转45度 
每次先把下列的元素先入队 当行坐标j==0时,再把下一行(i+1,j)入队
直观上看 每次队里pop出来的坐标(i,j) 下一列只要存在 就入队 只有当j==0时 再入队下一行(i+1,j)
T(N) S(sqrt(N))
'''
def anti_diagonal_traversal(nums:list[list[int]]) -> list[list[int]]:
    queue = collections.deque([(0,0)])
    ret = []
    while queue:
        size = len(queue)
        cur_lvl = []
        for _ in range(size):
            i, j = queue.popleft()
            cur_lvl.append(nums[i][j])
            if j + 1 < len(nums[i]):
                queue.append((i, j + 1))
            if j == 0 and i + 1 < len(nums):
                queue.append((i + 1, j))
        ret.append(cur_lvl)
    return ret

# test
#nums = [[1,2,3], [4,5,6,], [7,8,9]]
#print(anti_diagonal_traversal(nums))