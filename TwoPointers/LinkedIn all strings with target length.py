'''
给定一条DNA序列 在里面里找出所有出现了多次的长度为10的子序列.

编码方案：
首先 需要一个高效的方式来表示DNA序列。DNA序列由A、C、G、T四个字母组成 我们可以用2位二进制数来表示每个字母
A: 00
C: 01
G: 10
T: 11

一个长度为10的子序列可以用20位来表示。

滑动窗口：
我们可以使用滑动窗口的方法 每次移动一个字符 生成新的长度为10的子序列。

位运算优化：
对于每个新的子序列 我们可以使用位运算来快速计算它的20位表示
左移2位 丢弃最左边的两位
在最右边添加新字符的2位编码

哈希表存储：
使用哈希表来存储每个子序列的出现次数。键是子序列的20位整数表示 值是出现次数。
结果收集：
遍历哈希表 找出所有出现次数大于1的子序列。
时间O(n) 空间O(n)
'''
from typing import List

def findRepeatedDnaSequences(s: str) -> List[str]:
    if len(s) <= 10:
        return []
    
    # 编码映射
    encode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    # 初始化结果集和哈希表
    result = set()
    seen = {}
    
    # 初始化前10个字符的编码
    curr = 0
    for i in range(10):
        curr = (curr << 2) | encode[s[i]]
    
    # 将第一个10字符序列加入哈希表
    seen[curr] = 1
    
    # 滑动窗口
    for i in range(10, len(s)):
        # 更新当前编码：左移2位，移除最左边的字符，添加新字符
        curr = ((curr << 2) & 0xFFFFF) | encode[s[i]]
        
        if curr in seen:
            if seen[curr] == 1:
                result.add(s[i-9:i+1])
            seen[curr] += 1
        else:
            seen[curr] = 1
    
    return list(result)

# Example usage
dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
repeated_sequences = findRepeatedDnaSequences(dna_sequence)
print(repeated_sequences)