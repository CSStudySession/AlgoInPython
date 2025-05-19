'''
思路:双指针left和right来维护一个滑动窗口 [left, right]
- 每次移动r扩大窗口 一旦窗口内包含了至少一个 'a'、一个 'b' 和一个 'c'
就说明当前窗口 [left, right] 是一个合法子字符串
- 同时 从l开始的更长的所有子字符串[left, right],[left, right+1], ...,[left, len(s)-1]都是合法的
T(n) S(1)
'''
def numberOfSubstrings(self, s: str) -> int:
    left, right, total = 0, 0, 0
    freq = [0] * 3 # track frequency of a, b, c
    while right < len(s):
        freq[ord(s[right]) - ord("a")] += 1 # update r freq
        while self.check_valid(freq): # While we have all required characters
            total += len(s) - right # [l,r]合法 那么[l,r]一直到end的字符串都会合法
            freq[ord(s[left]) - ord("a")] -= 1 # 收缩左窗口
            left += 1
        right += 1 # r要更新
    return total
def check_valid(self, freq: list) -> bool:
    # Check if we have at least one of each character
    for cur in freq:
        if cur == 0: return False
    return True
