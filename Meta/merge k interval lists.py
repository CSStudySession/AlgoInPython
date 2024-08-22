'''
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=1073573&page=1#pid19674457
求 intersection of K lists of intervals
我们定义了一个辅助函数 merge_two_interval_lists 用于合并两个区间列表并找出它们的交集。
在主函数 find_intersection 中，我们使用分治的思想：
如果只有一个列表，直接返回。
否则，将列表分成两半，分别递归处理。
最后，合并两个子问题的结果。

时间复杂度分析：
假设有 k 个列表，总共有 n 个区间。
合并两个列表的时间复杂度是 O(n)，因为我们只需要遍历一次两个列表。
我们需要进行 log k 次合并操作（因为每次都将问题规模减半）。
因此，总的时间复杂度是 O(n log k)。

空间复杂度分析：
递归调用栈的深度是 O(log k)。
在每一层递归中，我们都需要 O(n) 的空间来存储中间结果。

另一种解法: for each interval list[i] 与第i-1个interval list merge
时间复杂度O(k*n) 
'''
from typing import List

def merge_two_interval_lists(list1:List[int], list2:List[int]):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        # 找到两个区间的交集
        start = max(list1[i][0], list2[j][0])
        end = min(list1[i][1], list2[j][1])
        # 如果有交集，添加到结果中
        if start <= end:
            result.append([start, end])
        # 移动指针
        if list1[i][1] < list2[j][1]:
            i += 1
        else:
            j += 1
    return result

def find_intersection(intervals:List[List[List[int]]]) -> List[List[int]]:
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals[0]
    
    # 使用分治法
    mid = len(intervals) // 2
    left = find_intersection(intervals[:mid])
    right = find_intersection(intervals[mid:])
    
    # 合并两个结果
    return merge_two_interval_lists(left, right)

# 测试用例
intervals1 = [
    [[1,5], [10,14], [16,18]],
    [[2,6], [8,10], [11,20]],
    [[3,7], [9,12], [15,19]]
]

intervals2 = [
    [[0,2],[5,10],[13,23],[24,25]], 
    [[1,5],[8,12],[15,24],[25,26]]
]

intervals3 = [
    [[1,3],[5,9]],
    []
]
print(find_intersection(intervals1)) # [[3, 5], [10, 10], [11, 12], [16, 18]]
print(find_intersection(intervals2)) # [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
print(find_intersection(intervals3)) # []