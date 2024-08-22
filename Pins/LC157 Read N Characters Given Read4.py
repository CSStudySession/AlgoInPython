'''
https://leetcode.com/problems/read-n-characters-given-read4/description/
'''
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from typing import List

def read4(buff: List[str]) -> int:
    pass

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [""]*4
        total = 0 #total已经read了多少个char
        while total < n:
            count = read4(buf4) # Read file into buf4 && count 
            if count == 0: break #需要break
            count = min(count, n - total) # n-total: 还剩多少char可以读入(read)
            
            buf[total:] = buf4[:count]
            total += count #total走到下一次读的开始位置

        return total
