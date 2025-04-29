
'''
归纳:(val(i) - i - 1)可以得出 在idx i之前 一共丢失了几个数字
假如通过二分 找到了某个idx==m 使得:val(m)-m-1==k 根据上述观察 在idx==m之前丢了k个数字
下一步需要知道这第k个丢失数是什么
如果不丢数: val(i)==i+1
数与数之间 如果每丢一个数 下一个数字数值就比丢失的这个数大1 举例: 
idx: 0	 1	 2	 3
val: 1	 3	 6	 8
val1和3之间丢了2 如果k==1 二分最终停在idx==1 缺的数字就是二分停止的idx+1==2

所以如果在idx==m上 已知丢了k个数 那么第k个丢掉的==m + k

注意上面所有的论述是假设 二分停止的idx之前一定是有缺数字的 即:要找的miss num < 当前的val(idx)
还有一类情况是 没有缺数字 或者说 要找的数字是在idx的右边 此时二分停止的位置指向数组最大值(也就是最靠近missing num的位置)
这时miss num == idx+1+k, 其中idx+1是当前位置不缺数的情况下理论上的数值 需要再往右数k个得到missing num 
'''
def findKthPositive(self, arr: list[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - mid - 1 < k: # mid之前缺的数小于k mid和左边都不是答案
            left = mid + 1
        else:
            right = mid
    if arr[right] > right + k: # 如果right之前缺数字 right+k是理论上缺的第k个数字
        return right + k
    else:                      # 否则right停在arr[-1]
        return right + k + 1

'''
variant: return kth missing number starting from the leftmost num of array.
-- 对比原题是从1开始算
另一种问题描述: given nums as a list of holidays that you can't work, and k as the num
of days required to complete a project. find the fist day a project can be finished.
'''
def findKthPosMissing(arr: list[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] - mid - arr[0] < k: # mid之前缺的数小于k mid和左边都不是答案
            left = mid + 1
        else:
            right = mid
    if arr[right] > right + k: # 如果right之前缺数字
        return right + k + arr[0] - 1
    else:                      # 否则right停在arr[-1]
        return arr[0] + right + k

# test
arr = [4,7,9,10]
k = 1  # 5

arr = [4,7,9,10] # 8
k = 3

arr = [1,2,5] # 7
k = 4

print(findKthPosMissing(arr, k))
