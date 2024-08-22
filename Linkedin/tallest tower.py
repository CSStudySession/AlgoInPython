'''
suppose you are trying to build a very tall tower. you have a collection of blocks to make your tower out of. 
For each block type, you are given the numbers of blocks you have of that type, its weight, and the max. weight 
that block can support above it and including itself. suppose for now that all blocks have the same height(1 meter). 
what's the tallest tower you can construct by stacking these blocks?

Example input, with each row representing a block type of format: number of blocks, weight, max support weight:
[ [1, 1, 1], [100, 3, 100], [10, 2, 10]]
Example output: 35
for this sample problem, the best solution is to stack the single (1,1) block on top, then 4 of (2,10) blocks under it, 
giving a total weight of 9; we can then stack 30 more (3, 100) blocks at the base. 


思路: dp
dp[i][j]表示使用前i种砖块 总重量为j时的最大高度
dp[i][j]可以由两种方式转移得来
1. dp[i-1][j]:不使用第i块砖
2. dp[i-1][j-k*weight[i]] for k:1,2,...count (当前砖可以用1,2,...count块)
两者取一个max 就是dp[i][j]
'''
from typing import List

def max_tower_height(blocks: List[List[int]]) -> int:
    # 按承重能力（max_support）从小到大排序
    blocks.sort(key=lambda x: x[2])
    
    n = len(blocks)
    # 所有blocks加在一起的总重量之和 是理论上dp[i][j]的j那一维的最大值
    max_weight = sum(block[0] * block[1] for block in blocks)
    
    # 初始化dp数组，dp[i][j]表示使用前i种砖块，总重量为j时的最大高度
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        count, weight, max_support = blocks[i-1]
        for j in range(max_weight + 1):
            # 不使用当前砖块
            dp[i][j] = dp[i - 1][j]
            
            # 尝试使用当前砖块
            for k in range(1, count + 1):
                # 当前重量是j 用了k块重weight的砖 所以之前的状态重量是:(j-k*weight)
                # 之前的状态必须合法 所以j-k*weight >= 0
                # 当前的重量必须要在当前砖的承受力之内:j<=max_support 
                if j >= k * weight and j <= max_support:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weight] + k)
    
    # 返回所有可能总重量中的最大高度
    return max(dp[n])

# 测试用例
blocks1 = [[1, 1, 1], [100, 3, 100], [10, 2, 10]]
result1 = max_tower_height(blocks1)
print(f"最大高度: {result1}")

blocks2 = [[4, 1, 10], [1, 9, 9], [4, 2, 18]]
result2 = max_tower_height(blocks2)
print(f"最大高度: {result2}")


# followup: 如果每块砖的高度不一样
# 还是按照承重能力从小到大排序
def max_tower_height_w(blocks):
    # 按(承重能力递增,高度递减)排序:先用 承重差且高度高的blocks
    blocks.sort(key=lambda x: (x[2], -x[3]))
    
    n = len(blocks)
    max_weight = max(block[2] for block in blocks)
    
    # 初始化dp数组
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        count, weight, support, height = blocks[i - 1]
        for w in range(max_weight + 1):
            dp[i][w] = dp[i-1][w]               # 不使用当前块
            
            # 尝试使用当前砖块 枚举可能用多少块当前砖
            for k in range(1, count + 1):
                if k * weight <= w and w <= support:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - k * weight] + k * height)
    
    return dp[n][max_weight]

# 测试样例
blocks = [[1, 1, 1, 2], [100, 3, 100, 1], [10, 2, 10, 3]]  # 答案是45 用5个blocks[2] 用30个blocks[1] 不用blocks[0]
result = max_tower_height_w(blocks)
print(f"能建造的最高塔楼高度为: {result}")

'''
def dfs(weight:int, index:int, blocks:List[List[int]], dp:List[List[int]]) -> int:
    # 基本情况：当没有更多砖块可用时
    if index == len(blocks):
        return 0
    
    # 如果已经计算过这种情况，直接返回结果
    if dp[weight][index] != -1:
        return dp[weight][index]
    
    # 不使用当前砖块
    result = dfs(weight, index + 1, blocks, dp)
    
    count, block_weight, max_support = blocks[index]
    
    # 尝试使用当前砖块
    if weight + block_weight <= max_support:
        for i in range(1, count + 1):
            if weight + i * block_weight > max_support:
                break
            result = max(result, i + dfs(weight + i * block_weight, index + 1, blocks, dp))
    
    # 存储结果
    dp[weight][index] = result
    return result

def max_tower_height(blocks: List[List[int]]) -> int:
    # 按重量升序排序
    blocks.sort(key=lambda x: x[2])
    
    n = len(blocks)
    max_weight = sum(block[0] * block[1] for block in blocks)
    
    # 初始化dp数组
    dp = [[-1] * n for _ in range(max_weight + 1)]
    
    return dfs(0, 0, blocks, dp)

# 测试用例
blocks = [[1, 1, 1], [100, 3, 100], [10, 2, 10]]
result = max_tower_height(blocks)
print(f"max height: {result}")

''' 