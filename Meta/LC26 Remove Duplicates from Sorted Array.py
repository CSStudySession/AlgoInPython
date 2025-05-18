'''
思路:二分. 要求in-place更新nums 使得不重复的元素都挪到前面
- 定义两个指针 cur指向下一个unique元素可以放置的下标 idx指向需要检查的数组下标
- idx从前往后扫 指向的元素通过二分找到最后一个位置 设为r 
- 把r的元素写到cur位置 idx移动到r+1(中间全是重复元素) cur+=1
- 循环停止时 cur恰好代表去重数组的长度(因为跳出循环前一刻cur+=1)
T(klog(n)) k是重复元素个数 S(1) 
'''
def removeDuplicates(nums: list[int]) -> int:
    cur, idx = 0, 0
    while idx < len(nums):
        target = nums[idx]
        left, right = cur, len(nums) - 1
        while left < right: # 二分找target的最后一个位置
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        nums[cur] = nums[right] # right一定存在 至少是idx本身
        idx = right + 1 # idx指向r下一个 跳过中间重复的
        cur += 1 # cur指向下一个可写入的位置
    return cur