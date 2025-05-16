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