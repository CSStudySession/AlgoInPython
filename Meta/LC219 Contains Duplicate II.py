
# 用dict维护{见过的value: 最近一次出现的下标} 当前value去dict检查. 
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if not nums or len(nums) <= 1:
        return False
    val_to_idx = {}
    for i in range(len(nums)):
        cur = nums[i]
        if cur in val_to_idx:
            pre_idx = val_to_idx[cur]
            if i - pre_idx <= k:
                return True
        val_to_idx[cur] = i # 注意这里不能写else 每次都要更新dict
    return False