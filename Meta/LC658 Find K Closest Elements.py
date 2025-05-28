'''
因为数组有序 k个最接近x的元素一定是连续的 可以用二分查找窗口起点 窗口长度为k
那么窗口合法起点范围为[0, len(arr) - k]
二分时比较arr[mid]和arr[mid+k](右端点之外的下一个数)哪个更靠近x
  - 如果x - arr[mid] > arr[mid+k] - x 说明窗口右移更优 left=mid+1
  - 否则窗口应在当前或更左 right=mid
当left == right时 就是最优的起点 返回arr[left:left+k] 这k个数即可
T(log(n-k)) S(1)
'''
def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = (lo + hi) // 2
        if x - arr[mid] > arr[mid + k] - x: # 这里不加绝对值 x要么在窗口内 要么在窗口外 
                                            # 哪一种情况 这种写法都能cover 写绝对值反而不行
            lo = mid + 1 # 右端点下一个数更近 mid一定不是答案
        else:
            hi = mid    # 左端点mid更近 可能是答案
    return arr[lo:lo + k]