'''
https://leetcode.com/problems/count-and-say/description/?envType=company&envId=pinterest&favoriteSlug=pinterest-six-months

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).

思路: 按照定义中给出的公式 一步步模拟迭代即可
复杂度分析:
内层循环：每次迭代处理前一次生成的字符串 ret。
最坏情况下, ret 的长度在每次迭代中可能增加一倍。
第 i 次迭代中, ret 的长度可能达到 2^(i-1)。
总体时间复杂度：
O(2^1 + 2^2 + ... + 2^(n-1)) = O(2^n)
这是因为每次迭代的复杂度都可能是前一次的两倍。

空间复杂度：
ret 和 tmp 字符串：
在最坏情况下，最终的字符串长度可能达到 O(2^n)。
其他变量（如 cur_len, idx, cnt): 使用常量空间 O(1)。
总体空间复杂度: O(2^n)
主要的空间消耗来自于存储生成的字符串。
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        if not n:
            return ""
        
        ret = "1" # base case
        for i in range(2, n + 1): # 1就是base case 从2开始遍历到输入的n
            tmp = ""
            cur_len, idx = len(ret), 0 # 根据定义 遍历当前的ret 遍历过程中找重复字符 并用cnt记录
            while idx < cur_len:
                cnt = 1
                while idx + 1 < cur_len and ret[idx] == ret[idx + 1]:
                    cnt += 1
                    idx += 1
                tmp += str(cnt) + ret[idx] # idx会停在最后一个重复的字符位置:idx+1与idx字符不同
                idx += 1 # 处理下一个字符
            ret, tmp = tmp, ret # 每次处理完一步 需要把ret更新为当前的tmp
        return ret