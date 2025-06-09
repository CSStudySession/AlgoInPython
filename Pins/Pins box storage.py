'''
给定一个一维存储区 有固定数量的shelves 每个架子有一个最大高度限制
你有一组boxes 每个箱子也有一个高度 目标是将尽可能多的箱子放入架子中 或达到某种优化目标(follow-up questions)
-- 规则：架子从左到右排列 不能换顺序, 每个架子最多放一个箱子, 箱子不能堆叠, 箱子可以按任意顺序插入（可排序）
箱子只能从左往右推 不能回退. 如果一个箱子遇到比它高度低的架子（瓶颈）, 就不能通过。
输入输出：
输入: shelfHeight: List[int]：每个架子的高度限制(固定顺序), boxHeight: List[int]:箱子的高度数组（升序）
输出: 主问题:最多能放多少个箱子, Follow-up1:放入箱子的最大总高度, Follow-up2:从左右两端都可以推入箱子时 能得到的最大总高度
clarifications:
- 为何不能通过矮架子？ 若左边的架子比箱子矮，箱子就会卡住无法继续。
- 箱子不能穿越已放置的箱子。
- 架子固定顺序 箱子可以排序 可以假设已经sorted吗?
注意下面的所有code 假设box数组已经sorted. 如果没有 需要手动box.sort(). 时间复杂度会bounded在sort这里.
'''
'''
1. 最多放入多少个箱子?
思路:构造一个数组min_h[i] 表示第i个位置及其左边的最小的shelf高度(代表能到达i的 最大可能的box高度)
从右往左遍历min_h 尽量将小的箱子放入靠近右边的空位置->给稍大的箱子留更多机会往左边放. 因为一个位置一旦放了箱子,
它右边就不可能再放箱子了.
m=len(shelf) n=len(box) T(m+n) S(m)
'''
def fitBoxes(shelfHeight, boxHeight):
    m = len(shelfHeight)
    min_h = [0] * m
    min_h[0] = shelfHeight[0]
    # 构造 minHeight 数组
    for i in range(1, m):
        min_h[i] = min(min_h[i - 1], shelfHeight[i])
    idx, cnt = 0, 0 # 当前待放箱子（boxHeight 已排序）, 已放置的箱子数
    # 从右往左遍历
    for i in range(len(min_h) - 1, -1, -1):
        cur_limit = min_h[i]
        if idx < len(boxHeight) and boxHeight[idx] <= cur_limit:
            cnt += 1
            idx += 1
    return cnt

'''
followup1:使得总的箱子高度最大
思路:先放高的箱子 从右往左放, 目标是选出高度尽可能高, 但仍能放进去的箱子
n=len(shelf) m=len(box) T(m+n) S(n)
'''
def fitBoxesMaxHeight(shelfHeight, boxHeight):
    n = len(shelfHeight)
    min_h = [0] * n
    min_h[0] = shelfHeight[0]
    # 构造 minHeight 数组
    for i in range(1, n):
        min_h[i] = min(min_h[i - 1], shelfHeight[i])

    boxHeight.reverse()  # 先放高箱子 让box从大到小排序
    idx, total_h = 0 # 当前待放的箱子idx, 放置的总高度
    for i in range(len(min_h) - 1, -1, -1):
        while idx < len(boxHeight) and boxHeight[idx] > min_h[i]:
            idx += 1
        if idx < len(boxHeight):
            total_h += boxHeight[idx]
            idx += 1 # idx不用每次i循环重置 min_h是个不增数组 前面不满足的h 后面一定也不会满足
    return total_h

'''
followup2:两边都能推入箱子 求最大高度.
思路:双指针，维护左/右最小高度. 每次从两端选一个能放箱子的位置 把最大的箱子往里面放
m=len(shelf) n=len(box) T(m+n) S(1)
'''
def fitBoxesTwoEnds(shelfHeight, boxHeight):
    n = len(shelfHeight)
    left_minh, right_minh = shelfHeight[0], shelfHeight[-1]
    left, right = 0, n - 1
    total_h = 0
    boxHeight.reverse()  # 从最大箱子开始
    idx = 0
    while boxHeight and left <= right:
        while idx < len(boxHeight) and boxHeight[idx] > left_minh and boxHeight[idx] > right_minh:
            idx += 1  # 跳过高的箱子
        if idx == len(boxHeight): # 找不到合适的箱子
            break
        if boxHeight[idx] <= left_minh:
            total_h += boxHeight[idx]
            left += 1
            idx += 1
            left_minh = min(left_minh, shelfHeight[left] if left < n else float('inf'))
        elif boxHeight[idx] <= right_minh:
            total_h += boxHeight[idx]
            right -= 1
            idx += 1
            right_minh = min(right_minh, shelfHeight[right] if right >= 0 else float('inf'))
    return total_h

# test
shelf = [5, 2, 4, 3]
box = [2, 3, 4]
print(fitBoxesTwoEnds(shelf, box)) # 9