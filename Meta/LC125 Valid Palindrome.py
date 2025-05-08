'''
思路:双指针.左右指针分别跳过非isalnum()的元素 当两个指针的lower()不相等时 直接返回Flase
否则各走一步. 最后指针相遇时返回True
'''
def is_palindrome(s: str) -> bool:
    if not s: return True
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

'''
variant:回文条件修改成 if after excluding any characters outside of a given vector of characters "include", 
it reads the same forward and backward.
思路:双指针+检查当前字符是否在given include中
T(n) S(m) m is len of include
'''
def is_palindrome(s: str, include:list[str]) -> bool:
    if not s: return True
    include_set = set(include)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left] not in include_set:
            left += 1
        while left < right and s[right] not in include_set:
            right -= 1
        if left < right and s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True