'''
在新 pin 的描述中包含用户关注的关键词时，对相关用户发送提醒。
输入：一组 pin 对象，每个包含：
id: pin 的唯一标识
details: 描述字符串
username: pin 所属用户
一组usernames: 我们关心的用户名
一组keywords: 关键词，用户对这些关键词感兴趣
输出：返回所有来自上述用户名的 pin 中，其 details 包含关键词的 pin。
Clarifications:
用户名最大长度为 64
最多允许 100 个用户，每个用户最多设置 1000 个关键词（总共最多 100,000 个关键词）
关键词 可以包含空格
匹配 支持子串 "andy" 可以匹配 "candy"
关键词在所有用户之间共享（全局关键词）
输入未排序:No pre-sorting
思路: Trie + 关键词的每个字符当作起点匹配
1. 把关键词插入trie树
2. 过滤出针对target users的pins
3. 对每个pins的描述 每个字符当作起点进行matching.
K:关键词总长度 P:pins数量 D:平均desc的长度 -> T(K + P + P*D*D) S(K + P)
'''
class TrieNode:
    def __init__(self):
        self.children = {}  # 存储子节点：key=字符, value=TrieNode
        self.end = False    # 是否是一个完整单词的结束

def insert_keyword(root, keyword):
    node = root
    for ch in keyword:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.end = True  # 标记关键词结束

def should_trigger_alert(description, root):
    n = len(description)
    for i in range(n): # 每个字符都当作起点 进行尝试
        node = root
        j = i
        while j < n and description[j] in node.children:
            node = node.children[description[j]]
            if node.end:
                return True  # 匹配到了某个关键词
            j += 1
    return False  # 所有起点都没有匹配

def get_alert_pins(pin_list, target_users, keyword_list):
    trie_root = TrieNode()
    for word in keyword_list: # build trie
        insert_keyword(trie_root, word)
    
    filtered_pins = [] # 过滤出属于目标用户的pins
    for pin in pin_list:
        if pin['username'] == target_users:
            filtered_pins.append(pin)
    
    ret_pins = [] # 检查pin的描述是否包含关键词
    for pin in filtered_pins:
        if should_trigger_alert(pin['details'], trie_root):
            ret_pins.append(pin)
    return ret_pins

