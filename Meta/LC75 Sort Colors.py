'''
三指针 i,j,k 维护数组 使得:
[0,j-1]全是0, [j,i-1]全是1, [k+1, end]全是2
<-----><------->|-----------|<------>end
      j        i   area  k
i往右移动时 三种情况: (初始化i,j==0 k==end)
1.a[i]==0 此时与j对应的元素交换 i,j各走一步
2.a[i]==1 满足最终要求 不需要交换 i走一步往前继续探索
3.a[i]==2 此时与k对应元素交换 k往左走一步 但i不动 因为k换过来的元素不确定是什么 不能动
当i,k交叉 即k=i-1时 循环结束
T(n) S(1)
'''
def sortColors(nums: list[int]) -> None: # in-place modification.
    if not nums:
        return
    i, j, k = 0, 0, len(nums) - 1
    while i <= k:
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[i] == 1:
            i += 1
        else: # nums[i] == 2
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1
    return


