'''
思路:二分. 原有序数组被切了一下 没法直接二分 所以分两步:
1. 先二分找到pivot的点 
2. 通过target与nums[0]的大小关系 判断target落到切成两段的哪一段 在对应段进行二分
T(logn) S(1)
'''
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right: # 二分找到pivot的点 数组分成两段[l,p] [p+1,r]
        mid = (left + right + 1) // 2
        if nums[mid] > nums[0]:
            left = mid
        else:
            right = mid - 1

    if target >= nums[0]: # 目标落在[l,p]区间
        left, right = 0, right
    else: # nums只有一个数时 left,right会交叉 故返回时用right 不会越界
        left = right + 1 # 目标落到[p+1,r]区间
        right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right if nums[right] == target else -1