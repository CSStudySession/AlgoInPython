
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        for i in range(len(num_str)  - 1):
            if num_str[i] < num_str[i + 1]: # 从前往后找到第一个非递减的位置
                pivot = i + 1 
                for j in range(i + 1, len(num_str)):
                    if num_str[j] >= num_str[pivot]: # 从i+1的位置往后找最大的一个数 有相等的数且越往后越好(>=)
                        pivot = j
                for k in range(i + 1):               # 从[0,i]找第一个比pivot小的数 两数交换
                    if num_str[k] < num_str[pivot]:
                        num_str[k], num_str[pivot] = num_str[pivot], num_str[k]
                        return int("".join(num_str)) # 注意这里的写法 --> "".join(List)
        return num