'''
Given a list of words find the shortest unique prefix for each word such that 
the prefix uniquely identifies it among all words. 
The shortest unique prefix is the minimum starting substring that 
differentiates the word from the rest. Return the result list in the same order of the input.
Constraints
1 ≤ words.length ≤ 10⁵
1 ≤ words[i].length ≤ 100
Each word consists only of lowercase English letters ('a' - 'z').
No word in the list is a prefix of another, ensuring each word can have a unique prefix.
Example 1:
Input: words = ["zebra", "dog", "duck", "dove"]
Output: ["z", "dog", "du", "dov"]
Explanation: For "zebra", since no other word starts with 'z', the unique prefix is "z". 
For "dog", the letter "d" is common with "duck" and "dove", so the prefix is extended to "dog". 
Similarly, "duck" requires "du" and "dove" needs "dov" to be uniquely identified.
Example 2:
Input: words = ["codetest", "code", "coder", "coding"]
Output: ["codet", "code", "coder", "codi"]
Example 3:
Input: words = ["a", "ab", "aab", "abc", "aabc", "def"]
Output: ["a", "ab", "aab", "abc", "aabc", "d"]

思路:使用Trie查找每个单词的唯一前缀
- 构建Trie 每个节点记录该前缀被多少个单词经过 count
- 查找唯一前缀 对每个单词 从Trie根开始向下走 记录路径上字符
一旦某个节点的count==1 说明当前路径是唯一前缀

N is len(words) L is avg word length
build trie T(N*L) search T(N*L)  S(N*L)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # 表示有多少单词经过这个节点

def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
        node.count += 1  # 每个节点记录路径经过的单词数量

def find_unique_prefix(root, word):
    node = root
    prefix = ""
    for char in word:
        prefix += char
        node = node.children[char]
        if node.count == 1:
            break  # 当前前缀已经足够唯一
    return prefix

def shortest_unique_prefix(words): # 顶层函数入口 调用trie
    root = TrieNode()
    # 构建Trie树
    for word in words:
        insert_word(root, word)
    # 查找每个单词的最短唯一前缀
    result = []
    for word in words:
        prefix = find_unique_prefix(root, word)
        result.append(prefix)
    return result


# test
words = ["zebra", "dog", "duck", "dove"]
words = ["codetest", "code", "coder", "coding"]
words = ["a", "ab", "aab", "abc", "aabc", "def"]
print(shortest_unique_prefix(words))