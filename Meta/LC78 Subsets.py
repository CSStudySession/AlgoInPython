# input has no duplicates
'''
1. 定义一个递归函数 dfs(start, temp, ret, nums) 
ret存储所有的子集, temp是当前构造中的子集, start为当前递归在nums中的起始位置
2. 每次进入dfs都将当前的temp拷贝一份加入ret中
3. 然后从当前位置开始遍历剩下的元素 将元素加入temp 继续递归
4. 每次递归返回后需要执行temp.pop() 回溯到上一步状态 继续尝试其他分支
eg. nums = [1, 2]
start with []
[]
├── [1]
│   └── [1, 2]
└── [2]
T(n*2^n) S(n), 包含n个不同元素的集合 子集数量是2^n, 每个子集构造平均O(n)
'''
def subsets(nums: list[int]) -> list[list[int]]:
    if not nums:
        return [[]]
    tmp, ret = [], []
    dfs(0, tmp, ret, nums)
    return ret
def dfs(start, tmp, ret, nums):
    ret.append(tmp[:])
    for i in range(start, len(nums)):
        tmp.append(nums[i])
        dfs(i + 1, tmp, ret, nums)
        tmp.pop()