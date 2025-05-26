'''
给定一个数组intervals 其中每个元素都是一个包含两个整数的列表[a, b]
现在需要生成所有可能的n位数 其中n等于数组的长度
生成规则：
第1位数字必须从 intervals[0] 中选择
第2位数字必须从 intervals[1] 中选择
以此类推 第i位数字必须从 intervals[i-1] 中选择
生成的数字不能有前导零 返回的结果需要去重
示例1
输入: [[1,2], [3,4], [5,6]]
输出: [135, 136, 145, 146, 235, 236, 245, 246]
解释: 
- 第1位从[1,2]选择: 1或2
- 第2位从[3,4]选择: 3或4  
- 第3位从[5,6]选择: 5或6
- 所有组合: 1+3+5=135, 1+3+6=136, 1+4+5=145, 1+4+6=146, 
            2+3+5=235, 2+3+6=236, 2+4+5=245, 2+4+6=246
T(2^n) S(2^n)
'''
# 解法1:dfs. 每次dfs时 构造一位数 然后dfs构造下一位. 直到构造完所有位数后返回.
# 用pos记录构造的位数 dfs过程中把构造的数放在path数组中 最后统一转化成一个数值.
# S(2^n) set去重 最多可能有2^n个数. dfs层数最多n
def generate_n_digit_nums(intervals: list[list[int]]) -> list[int]:
    if not intervals:
        return []
    result = set()
    n = len(intervals)
    path = []
    dfs(0, path, n, intervals, result)
    return list(result)

def dfs(pos, path, n, intervals, result):
    if pos == n:
        # 将路径转换为数字（此时已保证无leading zero）
        num = 0
        for digit in path:
            num = num * 10 + digit
        result.add(num)
        return
    for digit in intervals[pos]:
        # 第一位不能为0
        if pos == 0 and digit == 0:
            continue
        path.append(digit)
        dfs(pos + 1, path, n, intervals, result)
        path.pop()

# 解法2: 逐位生成 从左到右 逐个位置构造数字
# 每一位都基于前面已构造的数字进行扩展 注意第一位不能为0 最后用set去除重复数字
def generate_n_digit_nums_loop(intervals: list[list[int]]) -> list[int]:
    if not intervals:
        return []
    # 从只包含0的单个数字开始
    current_numbers = [0]
    
    for pos, interval in enumerate(intervals):
        next_numbers = []
        for current_num in current_numbers:
            for digit in interval:
                # 第一位不能为0
                if pos == 0 and digit == 0:
                    continue
                new_num = current_num * 10 + digit
                next_numbers.append(new_num)
        current_numbers = next_numbers
    # 使用set去重
    return list(set(current_numbers))