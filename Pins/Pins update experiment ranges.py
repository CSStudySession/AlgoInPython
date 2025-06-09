'''
进行A/B实验时 将用户通过user ID hash到0~999共1000个bucket中
每个桶可分配给某实验组(如 control / enabled1 / enabled2)也可以未分配。
实验比例调整时 需最小化bucket的变动数量 以减少cross-exposure带来的污染
Part 1:找出未被分配的bucket
输入:
{
  'control': [0, 5, 12, 20, 21, ..., 99],
  'enabled1': [100, 101, ..., 199],
  'enabled2': [200, 201, ..., 299]
}
输出:
[1, 2, 3, 4, 6, 7, ..., 998, 999] # 所有未在任何分组中的bucket

Part 2:根据当前和期望分配变更bucket
输入：
当前bucket分配:cur_buckets:
{
  'control': [0, 1, ..., 99],
  'enabled1': [100, ..., 199],
  'enabled2': [200, ..., 299]
}
目标分配(desired_size)
{
  'control': 200,
  'enabled1': 200,
  'enabled2': 200
}
输出：
新的bucket分配方案 保留已有bucket尽可能不变 新增优先从unallocated bucket中选 其次从shrink group中释放。
clarification:
问题	                         解答
Q: 分配是否必须总和100%?	      不必须。可以有unassigned
Q: 新旧分配是否必须相同分组？	    是的，两个输入必须是同一组名集合(必须在相同的实验组集合上做resize 不支持新增/删除实验组。)
Q: 是否只处理两组？	              可以多个组，例子中出现了 enabled1 enabled2
Q: 分配比例改变会不会需要换组？	    是的 例如从50/50变成60/40会导致部分bucket转组
Q: 分配大小可以任意吗？	           任意 输入是well-formed (≤1000个bucket 总group一致)


'''
# n:# of experiments T(1000+n) ~= T(1000), 因为n<=1000 S(1)
def find_available_buckets(cur_buckets): # part 1
    all_buckets = set(range(1000))
    used_buckets = set()
    for buckets in cur_buckets.values():
        used_buckets.update(buckets)
    return sorted(all_buckets - used_buckets)


def update_buckets(bucket_map, target_size): # part 2
    free_set = set(range(1000))  # 所有可能的 bucket 值
    group_count = {}
    # 移除当前被占用的bucket 并记录每组大小
    for group, buckets in bucket_map.items():
        group_count[group] = len(buckets)
        for b in buckets:
            free_set.discard(b)
    free_list = list(free_set)
    # 如果需要顺序: free_list = sorted(free_set)
    freed_list = []
    # 从缩小的实验组中释放多余的 bucket
    for group, tgt in target_size.items(): # tgt:target
        diff = group_count[group] - tgt  # 缩小值
        while diff > 0:
            freed_list.append(bucket_map[group].pop())
            diff -= 1
        group_count[group] = tgt # 更新为shrink后的值
    # 给增长的实验组分配bucket 优先使用未分配的 其次用已释放的
    idx_free, idx_freed = 0, 0
    for group, tgt in target_size.items(): # tgt:target
        need = tgt - len(bucket_map[group]) # target number - 目前有的 = 还需要多少
        while need > 0:
            if free_list and idx_free < len(free_list):
                bucket_map[group].append(free_list[idx_free])
                idx_free += 1
            elif freed_list:
                bucket_map[group].append(freed_list[idx_freed])
                idx_freed += 1
            else:
                raise Exception("Not enough buckets available")
            need -= 1
    return bucket_map

# test
cur_buckets = {
    'control': list(range(0, 500)),        # control: 500 buckets
    'enabled': list(range(500, 1000))      # enabled: 500 buckets
}
desired_size = {
    'control': 400,                        # shrink by 100
    'enabled': 600                         # grow by 100
}
print(update_buckets(cur_buckets, desired_size))

'''
followup:
1.输出格式改成 range(如[0, 99])
2.校验输入是否合法( 如sum ≤ 1000)
'''
# 1 用helper把输出压缩成区间格式
def compress_ranges(bucket_list):
    if not bucket_list:
        return []

    bucket_list.sort()
    res = []
    start = prev = bucket_list[0]

    for b in bucket_list[1:]:
        if b == prev + 1:
            prev = b
        else:
            res.append([start, prev])
            start = prev = b
    res.append([start, prev])
    return res
# 然后在return之前把 bucket_map[group] 转为range格式
#    for group in bucket_map:
#        bucket_map[group] = compress_ranges(bucket_map[group])
#    return bucket_map

# 2. 在update_buckets()方法一开始 加入下面的input check
#def update_buckets(bucket_map, target_size):
#    if set(bucket_map.keys()) != set(target_size.keys()):
#        raise ValueError("Mismatch in group names between bucket_map and target_size")
#    if sum(target_size.values()) > 1000:
#        raise ValueError("Total target bucket count exceeds 1000")