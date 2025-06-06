'''
variant: input array has unique nums. 输入数组没有重复. leetcode原题可以有重复 是一个followup.
思路: 
1. sort输入数组 注意要用sorted() 生成一个新的sorted array 原数组最后要查找rank用
2. 用dict记录value:rank 
3. 遍历原数组 写根据dict找rank写入 注意这里用了直接写会原数组的方式 如果不允许 创建一个新的array即可 
T(nlogn) S(n)
'''
def arrayRankTransform(nums: list[int]) -> list[int]:
    # 直接对原数组排序得到排名顺序
    sorted_nums = sorted(nums)  # 返回排序后的新列表 不影响原nums
    # 构建数值到排名的映射（因为值唯一，不需要考虑重复）
    num_to_rank = {}
    for i in range(len(sorted_nums)):
        num_to_rank[sorted_nums[i]] = i + 1  # 排名从 1 开始
    # 直接在原数组上修改
    for i in range(len(nums)):
        nums[i] = num_to_rank[nums[i]]
    return nums

'''
followup:输入数组可以有重复. allow duplicates.
思路:与上面题一样 只是sorted()的时候 传入去重后的arr 可以用sorted(set(arr)) 其他全一样
T(nlogn) S(n)
'''
def arrayRankTransform_duplicates(arr: list[int]) -> list[int]:
    if not arr:
        return []
    num_to_rank = {}
    nums = sorted(set(arr))
    rank = 1
    for num in nums:
        num_to_rank[num] = rank
        rank += 1
    for i in range(len(arr)):
        arr[i] = num_to_rank[arr[i]]
    return arr

'''
TODO: 2D的
'''