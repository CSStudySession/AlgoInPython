'''
backtrack+number pick
- 两步选择 dfs选区间i 再选区间j (i < j)
- 每步两个选项 每个区间有2个数字可选
  - 约束处理 十位不能为0 用set去重
T(n^2) S(n^2)主要来自set dfs栈深度最多是2 
如果输出保证是2位数 可以用定长bool aary优化: 
  - has_num=[False]*100 每次add时先看是不是True
'''
def generate_nums(intervals:list[list[int]]) -> list[int]:
    path, ret = [], set()
    idx = 0
    dfs(idx, path, ret, intervals)
    return ret

def dfs(idx, path, ret, intervals):
    if len(path) == 2:
        first, second = path
        num = 10 * first + second
        ret.add(num)
        return
    for i in range(idx, len(intervals)):
        for digit in intervals[i]:
            if len(path) == 0 and digit == 0:
                continue
            path.append(digit)
            dfs(i + 1, path, ret, intervals) # 注意是i+1不是idx+1
            path.pop()

itv = [[1,3], [2,4], [3,4]]
print(generate_nums(itv))