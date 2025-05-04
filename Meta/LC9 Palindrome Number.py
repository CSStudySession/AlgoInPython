
# 1. reverse the input int x  2. 比较 if origin == reversed
def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    original = x # 后面要in-place改x 先存一下
    reversed = 0
    while x > 0:
        remainder = x % 10
        reversed = reversed * 10 + remainder
        x = x // 10
    return original == reversed