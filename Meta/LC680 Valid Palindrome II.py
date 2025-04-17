'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
'''

# time O(n) space O(1)
def validPalindrome(s: str) -> bool:
    if not s:
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]: # 要么左边跳过当前字符 要么右边跳过当前字符
            if is_palindrome(left + 1, right, s) or is_palindrome(left, right - 1, s):
                return True
            else: # 只有一次跳过的机会.尝试跳过不成功,直接return False
                return False
        else:
            left += 1
            right -= 1
    return True

def is_palindrome(i, j, s) -> bool:
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True