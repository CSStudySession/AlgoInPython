'''
https://www.1point3acres.com/bbs/thread-896361-1-1.html
给一个generator 每次输出类似'abc\nde' 可能有多个'\n'或者没有. 要求写一个wrapper generator 每次输出一行

这道题类似read N chars from read4. 题目描述的很模糊 按照已有信息写一个LineReader类.

每次调用 readline():
readline() 方法中使用了一个 while 循环，当缓冲区 buffer 中没有 \n 时，
不断调用 read_func() 获取新的数据块chunk并追加到缓冲区中。

读取数据块的时间复杂度：假设 read_func() 每次返回的 chunk 大小为 C 那么追加 chunk 到缓冲区的操作是 O(C)。
查找换行符的时间复杂度：在缓冲区中查找 \n 的操作是 O(B)，其中 B 是当前缓冲区 buffer 的长度。
分割缓冲区的时间复杂度：当找到 \n 时，将缓冲区分割成两部分，一部分作为结果返回，另一部分留在缓冲区。这个操作也是 O(B)。

时间复杂度: O(N)，其中 N 是输入数据的总长度。
空间复杂度: O(N)，其中 N 是输入数据的总长度。
'''

class LineWrapper:
    def __init__(self, read_func):
        self.read_func = read_func
        self.buffer = ""

    def readline(self):
        while '\n' not in self.buffer:
            chunk = self.read_func()
            if not chunk:  # 如果读不到数据了
                if self.buffer:  # 返回缓冲区中剩余的数据
                    line = self.buffer
                    self.buffer = ""
                    return line
                return ""  # 没有剩余数据，返回空字符串

            self.buffer += chunk

        # 这里应该返回完整的行，并保留剩余的数据在缓冲区
        # 以'\n'为分隔符 分割成两个(第二个参数+1个)
        line, self.buffer = self.buffer.split('\n', 1)
        return line

# unit test
# 改进后的模拟函数
def read_chunk():
    # 模拟一次完整的读取过程
    data = ["abc\n", "de", "wefg\nasdf\n", "\n", "aaassf"]
    if read_chunk.index < len(data):
        chunk = data[read_chunk.index]
        read_chunk.index += 1
        return chunk
    else:
        return ""

# 初始化模拟函数的状态
read_chunk.index = 0

# 使用示例
wrapper = LineWrapper(read_chunk)

# 模拟多次调用
print(wrapper.readline())  # 输出: abc
print(wrapper.readline())  # 输出: dewefg
print(wrapper.readline())  # 输出: asdf 
print(wrapper.readline())  # 输出: (一个换行符)
print(wrapper.readline())  # aaassf