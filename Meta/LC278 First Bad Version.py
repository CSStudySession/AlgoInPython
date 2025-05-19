'''
思路:二分 找第一个出现的bad的下标.
T(logn) S(1)
'''
def firstBadVersion(self, n: int) -> int:
    if n <= 0:
        return
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return right   