'''
Input a method getRandom01Biased() that generates a random int in [0,1], where 0 is generated with probability p and 1 with 
(1-p).

output: a method getRandom06Uniform() that generates a random number in [0,6] with uniform probabiilty.
'''

import random
import math

def get_random01_biased() -> int:
    return 1 if random.random() > 0.3 else 0

def get_random01_uniformed() -> int:
    seed = get_random01_biased() + (get_random01_biased() << 1) # 区分01和10 如果不区分 两种情况加起来都是1
    if seed == 1:      # 1,0
        return 0
    elif seed == 2:    # 0,1
        return 1
    else:              # 非法组合 重新生成
        return get_random01_uniformed()    

def get_random06_uniform() -> int:
    # 把[0,6]之间的数字拆解成binary expression: 3 bits needed -> x = rand * 2^0 + rand * 2^1 + rand * 2^2
    seed = get_random01_uniformed() + (get_random01_uniformed() << 1) + (get_random01_uniformed() << 2)
    return seed if seed < 6 else get_random06_uniform()


'''
利用get_random01_uniformed() 均匀生成[x,y]区间内 任意的随机整数.
等价于生成一个[0, y-x]之间的数 最后返回时再加上x即可
'''
def get_randomxy_uniform(x:int, y:int) -> int:
    range_size = y - x + 1 # 区间长度
    if range_size <= 0: 
        raise ValueError("input range is invalid.")
    
    num_bits = math.ceil(math.log2(range_size)) # 计算出二进制表达区间长度 需要多少bits 向上取整
    while True:
        ret = 0
        cnt = num_bits
        while cnt: # 每次生成一位 然后左移 每一位都是均匀生成的 所以整体也满足均匀分布
            ret = (ret << 1) | get_random01_uniformed() # 当前ret左移一位 然后与生成的随机数按位取或
            cnt -= 1
        if ret < range_size: 
            return ret + x  

# print(get_randomxy_uniform(3,7))

'''
给定get_random01_uniformed() 要求get_random01_biased() 使得0的生成概率为p 1的生成概率为(1-p).

1. 多次调用 get_random01_uniformed() 来生成一个近似连续的、均匀分布在 [0, 1) 区间的随机数。这里使用了 32 次调用来获得较高的精度。
机理:
在二进制系统中 小数可以表示为:
0.b₁b₂b₃b₄... = b₁/2¹ + b₂/2² + b₃/2³ + b₄/2⁴ + ... 其中 bᵢ 是 0 或 1.
32 位提供了足够的精度（约 9 位十进制精度）通常足以满足大多数应用需求。

2. 通过比较这个随机数和给定的概率p 我们可以实现所需的偏置分布
当随机数小于p时返回0 否则返回1. 这确保了0出现的概率为p 1出现的概率为(1-p)

3. 如何测试? 测试函数通过大量试验来验证实际生成的概率是否接近目标概率.
'''
def get_random01_biased_from_01uniform(p: float) -> int:
    ret = 0.0
    for i in range(32): # 使用32位来近似连续值
        ret += get_random01_uniformed() * (1 / 2 ** (i + 1))
    # 比较随机值和给定的概率
    return 0 if ret < p else 1

def test_get_random01_biased_from_01uniform(p, num_trials=100000):
    count_0 = 0
    for _ in range(num_trials):
        if get_random01_biased_from_01uniform(p) == 0:
            count_0 += 1
    
    actual_p = count_0 / num_trials
    print(f"input p = {p}")
    print(f"actual p = {actual_p}")
    print(f"diff = {abs(p - actual_p)}")

test_get_random01_biased_from_01uniform(0.3)
test_get_random01_biased_from_01uniform(0.7)

# Variance: given random7 return random10
# Testing the rand10 function:
# 1. 先扔两次 产生49个数: num = ((first - 1) * 7 + second)
# 2. 如果num<40, return num%10 + 1 如果大于,重复random10.

import random

def rand7():
    return random.randint(1, 7)

def rand10():
    while True:
        num1 = rand7() - 1
        num2 = rand7() - 1
        result = num1 * 7 + num2  # Generates a number between 0 and 48
        if result <= 40:
            return (result % 10) + 1