'''
初始化两个指针 left = 0 和 right = n - 1。
初始化两个变量 maxLeft 和 maxRight 分别表示从左边和右边看到的最高柱子
每次比较 maxLeft 和 maxRight:
- 如果 maxLeft < maxRight 说明此时左边是瓶颈
 - 更新 maxLeft = max(height[left], maxLeft)
 - 当前能接的水量是 maxLeft - height[left]
 - 然后移动左指针
- 反之右边是瓶颈 类似处理
重复直到 left > right
为什么可以只看 maxLeft 和 maxRight 比较?
当前水位高度取决于较低的一侧 而较高的一侧即使再高 也无法限制水flow to lower side.
T(n) s(1)
'''
def trap(height: list[int]) -> int:
    water = 0
    maxLeft, maxRight = 0, 0
    left, right = 0, len(height) - 1
    while left <= right: # 这里一定要取到等号 相遇的位置 还没有被左边/或者右边处理过
        if maxLeft < maxRight:
            maxLeft = max(height[left], maxLeft)
            water += maxLeft - height[left]
            left += 1
        else:
            maxRight = max(height[right], maxRight)
            water += maxRight - height[right]
            right -= 1
    return water

'''
followup: what if some heights == -1, which means the water will leak?
有些柱子高度是 -1 无法承水
并且题目默认最左和最右两端也视为 -1 即不封闭 水会流走
所以水只能在两个-1之间的子段内积累
每两个-1之间 可以当作是原题的一个子问题来处理 对每个子数组段落单独计算积水量 最后累加即可
T(n) S(n) 用了辅助数组记录-1的位置
'''
def trapWithHoles(height: list[int]) -> int:
    # Step 1: 人为加虚拟的 -1 在头尾
    extended = [-1] + height + [-1]
    n = len(extended)
    # Step 2: 记录所有的 -1 位置
    boundaries = []
    for i in range(n):
        if extended[i] == -1:
            boundaries.append(i)
    total_water = 0
    for i in range(1, len(boundaries)):
        left = boundaries[i - 1]
        right = boundaries[i]
        if right - left <= 1:
            continue
        # 在 [left+1, right) 范围内处理，无需新建数组
        total_water += trap_segment(extended, left + 1, right - 1)
    return total_water

# helper 跟原题一样的逻辑
def trap_segment(nums, i, j):
    water = 0
    maxLeft, maxRight = 0, 0
    left, right = i, j
    while left < right:
        if maxLeft < maxRight:
            maxLeft = max(nums[left], maxLeft)
            water += maxLeft - nums[left]
            left += 1
        else:
            maxRight = max(nums[right], maxRight)
            water += maxRight - nums[right]
            right -= 1
    return water