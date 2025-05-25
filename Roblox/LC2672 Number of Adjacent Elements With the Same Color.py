'''
不需要每次重新遍历整个数组找相邻对 可以增量更新当前的相同颜色对数 具体方法如下：
1.记录当前数组num 初始为全0
2.用变量c记录当前的相邻颜色对数
3.每次更新颜色前 先看原位置nums[index]和其左右是否形成相同颜色对 是则先将对数减去
  - 然后更新颜色
  - 再判断新颜色和其左右是否形成新对 是则加上
T(q):每次查询O(1) 一共q次query  S(n):nums数组
'''
def colorTheArray(n, queries):
    nums = [0] * n  # 初始化数组
    c = 0  # 当前相邻颜色对数
    result = []
    for index, color in queries:
        # 获取 index 左右的颜色
        pre = nums[index - 1] if index > 0 else 0
        nex = nums[index + 1] if index < n - 1 else 0
        # 若当前位置已有颜色 与左右存在相同颜色对 需要先减去
        if nums[index] != 0:
            if nums[index] == pre:
                c -= 1
            if nums[index] == nex:
                c -= 1
        # 更新颜色
        nums[index] = color
        # 新颜色形成的相同颜色对，加上
        if nums[index] == pre:
            c += 1
        if nums[index] == nex:
            c += 1
        # 添加当前的对数
        result.append(c)
    return result