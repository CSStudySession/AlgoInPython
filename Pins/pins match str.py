'''
下面question 1/2 本质是一个题
question 1
Input有两个 一个是string的Array都是Pins e.g. ["Trump is winning", "Nvidia is a scam", "More men more fun"...]) 
另一个是一个user的rules e.g. ["Trump", "Nvidia", "Cars"] 
如果满足了一个rule就notify user 以上例子的话 前两个就会通知 (应该是一个substring matching的问题) 

"因为这个case下所有的rule都是一个word 我提出可以先parse然后用trie来做或者是rolling hash 
(当然也可以是KMP 但是楼主不熟故意没说) 我提出用rolling hash的话worst case要过所有的rules而且有collision风险 
所以建议用trie" 

question 2
给定两个list: 一堆blacklist的字串跟任意一个句子. 问句子是不是安全句子
安全的定義: 沒有出現完全符合blacklist字串裡頭的字. match blacklist word的規則是要完全match 不能夠partially的match
example:
blacklist of string: ["machine guns", "terrorist activity", "muder"]
input sentences (就是string)
a. "I bought a couple of machine guns yesterday." return False (不安全 machine guns在blacklist中)
b. "I suspect that man is a murderer." return True. (要求必须是一个完整的word匹配 不能是partial match 所以murderer不算匹配)

'''
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # insert a word into existing trie
    def insert(self, word:str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # check if a trie node exists in trie
    def find(self, word:str) -> 'TrieNode':
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    # check if word exists in trie as a whole word(exact match)
    def search(self, word:str) -> bool:
        node = self.find(word)
        return node is not None and node.is_word

    # check if word exists in tire, incuding a partial match
    def start_with(self, prefix:str) -> bool:
        return self.find(prefix) is not None
    
# for question 1
# 时间: 建Trie:O(len of rules) + 匹配O(len of pins)  空间: O(len of rules) for trie  
def string_match(pins:List[str], rules:List[str]) -> List[int]:
    ret = []
    if not pins or not rules:
        return ret
    
    # 构建trie
    root = Trie()
    for word in rules:
        root.insert(word)
    
    # 检查pins中的每一个单词
    # 这里根据题意可能稍微修改一下逻辑 不确定是pins[i]整体从头匹配 还是其中有个词match上就行
    for i in range(len(pins)):
        word_list = pins[i].split()
        for word in word_list:
            if root.search(word):
                ret.append(i)
                # print("match:", word)
    return ret

pins1 = ["Trump is winning", "Nvidia is a scam", "More men more fun"]
rules1 = ["Trump", "Nvidia", "Cars"]
print(string_match(pins1, rules1))

# for question 2
# 时间O(L+N^2 * M) L为黑名单单词总长度 N是句子中单词数 M是最长短语长度
# 空间O(L+N+M)
def is_safe_sentence(sentence:str, blocklist:List[str]) -> bool:
    if not blocklist or not sentence: # 没有规则或者没有输入 肯定“安全”
        return False
    
    # 构建trie
    root = Trie()
    for word in blocklist:
        root.insert(word.lower())
    
    # 将句子分割成单词
    words = sentence.lower().split()
    # 遍历sentence 检查每个单词是否在黑名单中
    for i in range (len(words)):
        cur_term = ""
        for j in range(i, len(words)):
            if j > i:
                cur_term += " "
            cur_term += words[j]
            if root.search(cur_term):
                return False
    return True

# unit test
blacklist = ["machine guns", "terrorist activity", "murder", "gun yesterday"]
sentences = [
    "I bought a couple of machine gun yesterday",
    "I suspect that man is a murderer"
]

for sentence in sentences:
    result = is_safe_sentence(sentence, blacklist)
    print(f"Sentence: '{sentence}'")
    print(f"Is safe: {result}\n")