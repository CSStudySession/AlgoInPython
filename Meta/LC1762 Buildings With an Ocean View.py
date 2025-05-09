'''
ocean在右边.要求返回有o view元素的下标 下标从小到大返回.
'''

'''
solution: monotolic stack. stack存下标 下标对应元素的高度单调增 stack top的高度最小
T: O(n)  S: O(n)
'''
def findBuildings(heights: list[int]) -> list[int]:
    if not heights:
        return []
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop() # 栈顶对应的高度<=当前高度 则栈顶一定没有o view
        stack.append(i)
    return stack

'''
variant1: return num of buildings have occean view.
思路:从右到左扫描 维护一个当前最高高度 若当前建筑高度 > 当前记录的最大高度
则该建筑可以看到海景 cnt += 1 并更新最大高度
T: O(n)  S: O(1)
'''
def num_of_buildings(heights: list[int]) -> int:
    if not heights:
        return 0
    max_height = heights[-1]
    idx = len(heights) - 2
    cnt = 1
    while idx >= 0:
        if heights[idx] > max_height:
            cnt += 1
            max_height = heights[idx]
        idx -= 1
    return cnt

'''
variant2: what if occean view is two sides? one has occean view if either side works.
the solution is required one pass: O(n)
思路:双指针 l, r 分别代表[0,l+1) (r-1, end]的处理过occean view的区间.
维护两个list left_view/right_view 分别存l,r扫过的左右区间中海景房的下标.
维护两个变量 left_max/right_max 分别代表l,r扫过区间的最高高度.
当l<r时 每次比较l/r_max 小的一边的指针移动(因为更可能找到海景房) 移动过程中更新max值.
注意代码中所有比较都是left<right 因为l,r每次都是"先走一步" 当相遇时 所有元素均已处理完
T(n) S(n)
'''
def two_side_occean_view(heights:list[int]) -> list[int]:
    if not heights:
        return []
    size = len(heights)
    if size == 1:
        return [0]

    left_view, right_view = [0], [size - 1]
    left_max, right_max = heights[0], heights[-1]
    left, right = 0, size - 1
    while left < right:
        if left_max < right_max:
            left += 1
            if heights[left] > left_max and left < right:
                left_view.append(left)
                left_max = heights[left]
        else:
            right -= 1
            if heights[right] > right_max and left < right:
                right_view.append(right)
                right_max = heights[right]
    return left_view + right_view[::-1]

# test
heights = [3, 1, 4, 1, 5]
print(two_side_occean_view(heights))