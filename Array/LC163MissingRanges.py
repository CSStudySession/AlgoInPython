'''
variant: print out result with given rules:
1. if there're more than one num in a missing range, use a '-' between two ends.
2. if there's one num in missing range, just print the num.
3. if there're exact two nums in a range, put them individually.

1. 补尾元素：
为了统一处理最后一个缺失区间 我们向nums末尾加入upper+1 避免一次特判.
2. 定义当前起始点cur_lower 用来追踪下一个缺失段的开始位置 初始为lower.
3. 遍历 nums:
  -对于每个 nums[i] 检查 cur_lower 到 nums[i] - 1 是否存在缺失值：
    -- 如果差值 > 2 说明有一段连续的缺失区间，如 5-9 用 '-' 表示。
    -- 如果差值 == 2 说明是两个单独缺失值 比如 5 和 6 分别加入。
    -- 如果差值 == 1 说明只有一个缺失数 直接加入。
    -- else: 没有缺失
4. 更新起点：
每次将cur_lower更新为nums[i] + 1 继续处理下一个缺失段

T(n) S(1)
'''
def get_missing_ranges(nums:list[int], lower:int, upper:int) -> list[str]:
    ret = []
    nums.append(upper + 1)
    cur_lower = lower
    for i in range(len(nums)):
        if nums[i] - cur_lower > 2:
            ret.append(str(cur_lower) + '-' + str(nums[i] - 1))
        elif nums[i] - cur_lower == 2:
            ret.append(str(cur_lower))
            ret.append(str(nums[i] - 1))
        elif nums[i] - cur_lower == 1:
            ret.append(str(cur_lower))
        cur_lower = nums[i] + 1
    return ret

# test
nums = [5, 8, 9, 15, 16, 18, 20]
lower, upper = 2, 87  # ['2-4', '6', '7', '10-14', '17', '19', '21-87']
nums = [5, 8, 9, 15, 16, 18, 20]
lower, upper = 1, 21  # ['1-4', '6', '7', '10-14', '17', '19', '21']
nums = [5, 8, 9, 15, 16, 18, 20]
lower, upper = 3, 20  # ['3', '4', '6', '7', '10-14', '17', '19']
print(get_missing_ranges(nums, lower, upper))

'''
OG. 思路:
遍历数组 比较相邻两个数字之间的差距 若差距大于1 则说明中间有缺失的数:可能是单个数字货区间
1. 把upper+1 append到nums末尾 避免特判
2. 定义一个cur_lower 初始值为lower 每次循环结束前 更新它为nums[i] + 1,这样统一判断逻辑:
  -- if nums[i] - cur_lower >=1 (>=1是因为cur_lower可以取到 可能是missing num)
T(n) S(1)
'''
def find_missing_nums(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    ret = []
    nums.append(upper + 1)
    cur_lower = lower
    for i in range(len(nums)):
        if nums[i] - cur_lower >= 1:
            ret.append([cur_lower, nums[i] - 1])
        cur_lower = nums[i] + 1
    return ret