'''
variant: 
Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap.
example:
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]
output [1,6], [8, 20]

思路:two pointer 
1)find the smaller one, assign to curr. 2)类似merge interval:比较res[-1]和curr for append
T(n+m) S(1)
'''
def mergeTwoIntervalList(firstList, secondList):
    i, j = 0, 0
    res = []
    while i < len(firstList) and j < len(secondList):
        first, second = firstList[i], secondList[j]
        if first[0] < second[0]:
            curr = first
            i += 1
        else:
            curr = second
            j += 1
        mergeIntervals(curr, res)
    
    while i < len(firstList):
        curr = firstList[i]
        mergeIntervals(curr, res)
        i += 1
    while j < len(secondList):
        curr = secondList[j]
        mergeIntervals(curr, res)
        j += 1      
    return res 

def mergeIntervals(curr, res):
    if not res or res[-1][1] < curr[0]:
        res.append(curr)
    else:
        res[-1][1] = max(res[-1][1], curr[1])
            
# test
A = [[1,5],[10,14],[16,18]]
B = [[2,6],[8,10],[11,20]]
print(mergeTwoIntervalList(A, B))

'''
算法思路：双指针遍历 + 交集判断
两个指针i和j分别遍历firstList和secondList
每次取出当前的两个区间first = firstList[i]和second = secondList[j] 判断是否有交集
交集的条件是 max(first[0], second[0]) <= min(first[1], second[1])
若成立 说明区间有交集 加入结果
然后移动较早结束的那个区间的指针:如果first[1]小于等于second[1] 则 i += 1 否则 j += 1
这样确保不会漏掉可能重叠的下一个区间。
边界处理 如果其中一个列表为空 则直接返回空列表
还加了一个预处理逻辑 如果firstList起始点更大 交换两个列表
T(m+n) S(1)
'''
def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    res = []
    if not firstList or not secondList: return res

    i, j = 0, 0
    if firstList[0][0] > secondList[0][0]:
            firstList, secondList = secondList, firstList
    while i < len(firstList) and j < len(secondList):
        first = firstList[i]
        second = secondList[j]
        maxStart = max(first[0], second[0])
        minEnd = min(first[1], second[1])
        
        if maxStart <= minEnd:
            res.append((maxStart, minEnd))
        if first[1] == minEnd:
            i += 1
        else:
            j += 1
    return res