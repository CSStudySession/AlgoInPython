'''
给定一个字符串数组 移除那些是其他字符串前缀的字符串 输出数组顺序要和输入顺序一致
输入：["ab", "abc", "abcd", "b", "bc"]
输出：["abcd", "bc"]

clarify: 1. all valid words, no spaces? 2. no duplication wrods?

思路:用Trie判断每个字符串是否是其他字符串的前缀
具体步骤:
- 将所有字符串插入Trie树
- 遍历原数组 判断每个字符串是否是其他字符串的前缀
  - 在Trie中搜索时 只要某个字符串的结尾不是叶子节点 说明它是其他字符串的前缀 需要移除
- 保留不是其他字符串前缀的字符串 顺序与原数组一致
Time-> 构建Trie O(N * L) N是字符串个数 L是平均长度 检查每个字符串是不是前缀 O(N * L)
总体O(N * L)
space-> Trie节点空间 最坏O(N * L)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        # self.is_end = False # 可以不写 这道题用不到
def insert_trie(root, word): # 把word插入以root为根的trie
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    # node.is_end = True
def is_prefix_of_others(root, word):
    node = root
    for char in word:
        node = node.children[char]
    # 如果结尾节点还有孩子，则是别人的前缀
    return len(node.children) > 0
def remove_prefix_strings(arr):
    root = TrieNode()
    # 先全部插入trie
    for word in arr:
        insert_trie(root, word)
    # 判断每个字符串是不是前缀
    result = []
    for word in arr:
        if not is_prefix_of_others(root, word):
            result.append(word)
    return result

# test
arr = ["app", "apple", "banana", "ban", "band", "bandit"]
arr = ["cat", "dog", "cats", "doge", "do"]
print(remove_prefix_strings(arr))