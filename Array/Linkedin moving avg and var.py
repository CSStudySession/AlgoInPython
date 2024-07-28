'''
大数据集上 如何计算avg和var? assume we have 500B samples(of type double)data, and we would like to calculate 
avg and var of it.

For avg: 
n * avg(x_n) + x_n+1 = (n+1) * avg(x_n+1)
-> avg(x_n+1) = ( (n+1)*avg(x_n) + x_n+1 - avg(x_n) ) / (n+1)  
              = avg(x_n) + (x_n+1 - avg(x_n)) / (n+1)
              上面的变换 是为了numerical stability 如果直接硬算 加法可能overflow!

For Var:
Var_n ^ 2 = Sum( (x_n - avg(x_n))^2 ) / (n - 1)  #注意这里是除n-1 一组含n个数的样本 自由度(degrees of freedom)是n-1
goal: define Var_n such that it only depends on x_n and var_n-1
after math derivation, we have: # 公式推导见notion
var_n+1 ^2 = (x_n+1 - avg(x_n))^2 / (n+1) + var_n ^2 * (n-1)/n
'''

import sys

class StreamingAverage:
    def __init__(self):
        self.avg = 0.0
        self.cnt = 0

    def calculate_avg(self, sample: float) -> float:
        self.cnt += 1
        self.avg += (sample - self.avg) / self.cnt  # 参看line 8的注释推导
        return self.avg
    
class StreamingVar:
    def __init__(self):
        self.avg = 0.0
        self.var = 0.0
        self.cnt = 0
    
    def calculate_var(self, sample: float) -> float:
        self.cnt += 1
        if self.cnt > 1: # 要判断cnt是否>1 
            self.var = (self.cnt - 2) / (self.cnt - 1) * self.var + (sample - self.avg) ** 2 / self.cnt
        
        self.avg += (sample - self.avg) / self.cnt
        return self.var # 这里可以返回both var and avg.      

# 终极优化 使用了Welford算法
# reference: https://changyaochen.github.io/welford/#numerical-stability
class RunningStats:
    def __init__(self):
        self.cnt = 0
        self.mean = 0.0
        self.mean_sqr = 0.0

    def update(self, x):
        self.cnt += 1
        delta = x - self.mean
        self.mean += delta / self.cnt
        delta2 = x - self.mean
        
        self.mean_sqr += delta * delta2

    def get_variance(self):
        if self.cnt < 2:
            return float('nan')  # 样本数量少于2时，方差无定义. 这里也可以返回0.0
        return self.mean_sqr / (self.cnt - 1)

    def get_mean(self):
        return self.mean

# 使用示例
welford = RunningStats()

# 模拟数据流
data_stream = [2, 4, 4, 4, 5, 5, 7, 9]

for value in data_stream:
    welford.update(value)
    print(f"Current value: {value}")
    print(f"Running mean: {welford.get_mean():.4f}")
    print(f"Running variance: {welford.get_variance():.4f}")
    print("---")

print(f"Final mean: {welford.get_mean():.4f}")
print(f"Final variance: {welford.get_variance():.4f}")