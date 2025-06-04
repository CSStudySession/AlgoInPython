'''
初始化两个指针 left = 0 right = n - 1。
每次比较 abs(nums[left]) 和 abs(nums[right])。
把更大的平方加入结果数组 res。
移动对应指针。
res reverse后 返回 翻转为升序
T(n) S(1)
'''
def sortedSquares(nums: list[int]) -> list[int]:
    res = []
    if not nums: return []
    left, right = 0, len(nums) - 1
    while left <= right:
        if abs(nums[left])>= abs(nums[right]):
            res.append(nums[left]*nums[left])
            left += 1
        else:
            res.append(nums[right]*nums[right])
            right -= 1
    res.reverse()
    return res
