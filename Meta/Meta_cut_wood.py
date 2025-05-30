'''
给你一个数组 L = [232, 124, 456] 表示木头长度 还有一个整数k 代表至少要切出k段长度相同的木头
每段的长度必须为整数。你可以对每根木头切任意次。
问你：最多能切出的木段长度是多少？
思路:二分 我们观察发现
如果某个长度x可以切出至少k段 那么所有小于x的长度也一定可以 因为可以切出更多段
如果某个长度x无法切出k段 那么所有大于x的长度也一定不行
这说明满足条件的段长具有单调性 可以用二分搜索 二分的目标是:满足条件的最大长度L
初始搜索范围为 [1, max(lengths)] 即最短段长是1 最长不会超过原始木头中最长的一根
每次计算中间值 mid = (left + right + 1) // 2
这样写是为了保证收敛时 left == right 是合法解 mid向上取整 防止endless loop
T(n*log(maxL)) 其中n是木头数量 maxL是最长木头  S(1)
'''
def wood_cut(lengths, k):
    if not lengths or sum(lengths) < k:
        return 0
    left, right = 1, max(lengths)
    while left < right:
        mid = (left + right + 1) // 2
        count = sum(length // mid for length in lengths)
        if count >= k:
            left = mid        # 当前mid满足条件 可能是答案 可以尝试更长的段 
        else:
            right = mid - 1   # 当前段太长 不能切出足够段数
    return right

# test
L = [232, 124, 456]
k = 7
print(wood_cut(L, k))  # 输出应为最大长度，比如114