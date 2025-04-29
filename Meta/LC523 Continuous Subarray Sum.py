
# 1. 给的数组元素是非负的 2. A-B==N*k 等价于 A,B对k同余
# 求前缀和 过程中用dict记录S_i%k(见过的余数)和对应下标
# T(N) S(N)
def checkSubarraySum(nums: list[int], k: int) -> bool:
    mod_to_idx = {0: -1} # 前0项和为0 对k取mod为0 对应下标-1(默认开始就满足)
    pre_sum = 0   # running prefix sum  
    for i in range(0, len(nums)):
        pre_sum += nums[i]
        if pre_sum % k in mod_to_idx:
            pre_idx = mod_to_idx[pre_sum % k]
            if i - pre_idx >= 2: # 之前出现的余数下标跟当前i有距离要求
                return True
        else:
            mod_to_idx[pre_sum % k] = i # 注意key是pre_sum%k
    return False