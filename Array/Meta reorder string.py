'''
输入一个字符串s 要求根据s里的字符出现的frequency从高到低重新排序。e.g. "mammamia" -> "mmmmaaai". 
如果字符出现次数相同，按字母表顺序排列相同频率的字符
'''

from collections import Counter

def frequency_sort(s: str) -> str:
    # Step 1: 统计每个字符的频率
    freq = Counter(s)
    
    # Step 2: 按照频率和字母顺序排序
    # 使用 (-freq[char], char) 作为排序键，先按频率降序，再按字母升序
    sorted_chars = sorted(freq.keys(), key=lambda ch: (-freq[ch], ch))
    
    # Step 3: 根据排序结果重构字符串
    result = ''.join(char * freq[char] for char in sorted_chars)

    # step 3 也能这么写
    #result = ''
    #for char in sorted_chars:
    #    result += char * freq[char]
    
    return result

# 测试
print(frequency_sort("mammamia"))  # 输出: "mmmmaaai"
print(frequency_sort("tree"))      # 输出: "eert"
print(frequency_sort("cccaaa"))    # 输出: "aaaccc"
print(frequency_sort("Aabb"))      # 输出: "bbAa"