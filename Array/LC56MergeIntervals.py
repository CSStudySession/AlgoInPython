from typing import List
'''
Time o(nlogn) for sorting, Space o(1)
if current interval does not overlap with the previous: append previous one to result.
else, if overlap: update previous ending to be max(current, previous)
'''
def merge(intervals: List[List[int]]) -> List[List[int]]:
    ret = []
    intervals = sorted(intervals) # sorted on first element of inner list
    prev_left, prev_right = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] > prev_right:
            ret.append([prev_left, prev_right])
            prev_left, prev_right = intervals[i][0], intervals[i][1]
        else:
            prev_right = max(prev_right, intervals[i][1]) # 注意这里只更新right 不能append. 后面可能还有重叠的intervals
    ret.append([prev_left, prev_right]) # last interval needs to process outside of for loop
    return ret

# variant: given two sorted array intervals A and B. intervals in A or B have no overlaps.
# merge intervals in A and B to one list of list.
def merge_intervals_in_two_array(A:List[List[int]], B:List[List[int]]) -> List[List[int]]:
    i, j = 0, 0
    ret = []
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][0]:
            cur = A[i]
            i += 1
        else:
            cur = B[j]
            j += 1
        merge_helper(cur, ret)
    while i < len(A):
        merge_helper(A[i], ret)
        i += 1
    while j < len(B):
        merge_helper(B[j], ret)
        j += 1
    return ret

def merge_helper(cur, ret):
    if not ret or cur[0] > ret[-1][1]:
        ret.append(cur)
        return
    ret[-1][1] = max(ret[-1][1], cur[1])

# test
A = [[3, 11], [14, 15], [18, 22], [23, 24], [25, 26]]
B = [[2, 8], [13, 20]]
# expected = [[2, 11], [13, 22], [23, 24], [25, 26]]
print(merge_intervals_in_two_array(A, B))
A = []
B = [[2, 8], [13, 20]]
# expected = [[2, 8], [13, 20]]
print(merge_intervals_in_two_array(A, B))