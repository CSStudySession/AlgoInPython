from collections import defaultdict
'''
varint:每个账号对应多个邮箱 邮箱有重合就表示账号相同 把相同的账号group起来并返回
input is a dict {str id: list of email strs}, e.g.:
{  A1: [alice@yahoo.com, alice_1@gmail.com], A2: [bob@facebook.com],
   A3: [alice_1@gmail.com, alice_2@hotmail.com], A4: [alice_2@hotmail.com]
   A5: [bob@facebook.com], A6: [carol@gmail.com] }
Output: ((A1,A3,A4), (A2,A5), (A6))

思路:
- 把邮箱当作图节点，账号里的邮箱之间相连
将每个账号中邮箱列表看作连通的节点
如果两个账号共享邮 它们的邮箱通过图连接在一起 
- DFS 遍历所有邮箱 标记属于同一连通分量的邮箱 → 再映射回账号
以邮箱为图节点 跑 DFS 找出所有连接的邮箱 
在每次 DFS 中，记录该连通块内所有邮箱属于哪个账号
用一个dict: email_to_id 表明某个邮箱归属于哪个代表账号
- 最后聚合同一连通分量内的所有账号ID 即最终合并结果 
N:账号数量  E:邮箱总数  M:邮箱之间的连接边数 总的图边数
T(N+E+M)   S(E+M+N)
'''
def accountsMerge(accounts):
    def dfs(adjs, email_to_id, visited, curr_email, id):
        visited.add(curr_email)  # 标记当前邮箱为已访问
        email_to_id[curr_email] = id  # 将当前邮箱归属到当前账号ID
        for adj in adjs[curr_email]:  # 遍历邻接邮箱
            if adj not in visited:
                dfs(adjs, email_to_id, visited, adj, id)  # 递归DFS相邻邮箱
    # Create adjacency list
    adjs = defaultdict(list)
    for id, emails in accounts.items():
        first_email = emails[0]  # 将第一个邮箱作为连接起点
        for email in emails[1:]:
            adjs[first_email].append(email)  # 建立无向边
            adjs[email].append(first_email)
    # Helper structures
    email_to_id = {}  # 记录每个邮箱所属的代表账号ID
    visited = set()   # 记录访问过的邮箱
    id_to_same = defaultdict(list)  # 存储合并后的账号ID分组
    # Perform DFS and group by connected components
    for id, emails in accounts.items():
        first_email = emails[0]
        if first_email in visited:
            same_id = email_to_id[first_email]  # 查找当前邮箱归属的代表账号
            id_to_same[same_id].append(id)  # 当前账号属于已存在的分组
        else:
            id_to_same[id] = []  # 当前账号作为新分组代表
            dfs(adjs, email_to_id, visited, first_email, id)  # DFS归类邮箱
    # Prepare result as a list of lists
    ret = []
    for id, same_ids in id_to_same.items():
        same = [id] + same_ids  # 合并同组账号ID
        ret.append(same)
    return ret

accounts = {
    "A1": ["alice@yahoo.com", "alice_1@gmail.com"],
    "A2": ["bob@facebook.com"],
    "A3": ["alice_1@gmail.com", "alice_2@hotmail.com"],
    "A4": ["alice_2@hotmail.com"],
    "A5": ["bob@facebook.com"],
    "A6": ["carol@gmail.com"]
}
print(accountsMerge(accounts))

'''
leetcode OG
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
["Mary","mary@mail.com"], ["John","johnnybravo@mail.com"]]

思路:
本质是一个图的 Connected Components 问题 我们将邮箱之间的关系建模成图：
每个邮箱是图的一个节点
如果两个邮箱出现在同一个账户中 它们之间有一条无向边
接下来通过 DFS 找出每个连通块（代表同一人的邮箱集合）然后再拼上用户名、排序即可。
1. build graph
对每个账户，把第一个邮箱 emails[0] 当作“代表邮箱”
把这个代表邮箱与其它邮箱双向连接（即构建无向边）
这样，账户内部的邮箱就全部联通了
2. dfs
用一个 visited 集合避免重复访问
对每个未访问的邮箱，启动 DFS 把同一个连通块内的邮箱全部加入 same_emails, 这些邮箱属于同一个人
3. build result
每当我们从一个新邮箱出发 DFS 说明发现了一个新的人, 把用户名 account[0] 拼上，同组邮箱排序后加入结果集
let A: # of accnt, E: # of email 
T(E + ElogE ~= ElogE)   S(E)
'''
def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    # 创建邮箱之间的图（邻接表）
    adj = defaultdict(list)
    for account in accounts:
        emails = account[1:]
        ref = emails[0]  # 选取当前账户的第一个邮箱作为“代表邮箱”
        for email in emails[1:]:
            # 建立无向边：代表邮箱 <-> 其它邮箱
            adj[ref].append(email)
            adj[email].append(ref)
    visited = set()  # 记录已访问的邮箱
    # 深度优先遍历，找出与当前邮箱相连的所有邮箱（一个连通块）
    def dfs(email, same_emails: list[str]):
        visited.add(email)
        same_emails.append(email)
        for nei in adj[email]:
            if nei not in visited:
                dfs(nei, same_emails)
    merged = []  # 存储合并后的账户结果
    # 遍历每个账户
    for account in accounts:
        emails = account[1:]
        if emails[0] in visited:
            # 该邮箱所在的连通块已访问过，跳过
            continue
        same_emails = []
        dfs(emails[0], same_emails)  # 从当前邮箱出发DFS 找到完整邮箱组
        # 将用户名与排序后的邮箱合并为一个账户
        merged.append([account[0]] + sorted(same_emails))
    return merged



'''Attention! 下面两个都是union-find的solution!!!
variant: 每个账号对应多个邮箱 邮箱有重合就表示账号相同 把相同的账号group起来并返回
input is a dict {str id: list of email strs}, e.g.:
{  A1: [alice@yahoo.com, alice_1@gmail.com], A2: [bob@facebook.com],
   A3: [alice_1@gmail.com, alice_2@hotmail.com], A4: [alice_2@hotmail.com]
   A5: [bob@facebook.com], A6: [carol@gmail.com] }
Output: ((A1,A3,A4), (A2,A5), (A6))
思路:Union-Find
1. 记录每个邮箱在哪些name下出现过 构建{email:[names]}索引
2. 将共享邮箱的人 用并查集合并
let N is num of accounts, E is num of emails 
time O(N+E) (find操作的时间复杂度近似常数)  space: O(N+E)
'''
def id_merge(accounts: dict[str, list[str]]) -> list[list[str]]:
    if not accounts:
        return [[]]
    # 记录每个邮箱在哪些name下出现过 构建{email:[names]}索引
    email_to_names = defaultdict(list)
    parent = {}
    for name, email_list in accounts.items():
        parent[name] = name # 初始化parent字典 每个人都以自己为根
        for email in email_list:
            email_to_names[email].append(name)
    # 将共享邮箱的人 用并查集合并
    # 同一个name_list里的所有人 统一放在name_list[0]的名字下面
    for name_list in email_to_names.values():
        root = name_list[0]
        for k in range(1, len(name_list)):
            parent[find_parent(parent, name_list[k])] = find_parent(parent, root)
    
    # 按相同的parent 把user group在一起
    # user_group: {parent: [userA, userB, userC...]} list里等于查重后 指向一个user
    user_group = defaultdict(list)
    for user, parent in parent.items(): # 注意user,parent顺序别反了
        user_group[parent].append(user)
    # 最后把相同的user集合取出来
    ret = []
    for user_list in user_group.values():
        ret.append(user_list)
    return ret 

def find_parent(parent:dict[str, str], name:str) -> str:
     # parent不是自己: 递归寻找parent 并把自己挂在first level parent上
     # 路径压缩
    if parent[name] != name:
        parent[name] = find(parent, parent[name])
    return parent[name]

# unit test
accounts = {"A1": ['alice@yahoo.com', 'alice_1@gmail.com'],
"A2": ["bob@facebook.com"],
"A3": ["alice_1@gmail.com", "alice_2@hotmail.com"],
"A4": ['alice_2@hotmail.com'],
"A5": ['bob@facebook.com'],
"A6": ['carol@gmail.com']}     
# print(id_merge(accounts))


# 原题. 思路:并查集 
def find(union: list[int], id: int) -> int:
    if union[id] != id: # 根不是自己: 递归寻根并把自己挂在一级根上(路径压缩)
        union[id] = find(union, union[id])
    return union[id]

def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    len_accnt = len(accounts)
    union = []
    for i in range(len_accnt): # 初始化union-find:每个account都以自己为根
        union.append(i)
    
    # 记录每个邮箱在哪些id下出现过 构建{email:[ids]}索引
    email_to_ids = defaultdict(list)
    for i in range(len_accnt):
        for j in range(1, len(accounts[i])): # 邮箱从第二个元素开始 第一个元素是人名
            email_to_ids[accounts[i][j]].append(i)

    # 将共享邮箱的ids利用并查集合并
    for id_list in email_to_ids.values():
        for k in range(1, id_list): # 同一个email下的所有id 都挂在id_list[0]下面
            union[find(id_list[k])] = find(id_list[0])

    # 把邮箱按照其在 u-f处理后的id所属的集合 加入到同一个set中
    sets = [set()] * len_accnt # [set1, set2, ...]
    for i in range(len_accnt):
        for j in range(1, len(accounts[i])):
            sets[find(i)].add(accounts[i][j])

    # 把含有邮箱的set中的元素加入到最终答案中
    ret = []
    for j in range(len_accnt):
        if sets[j]:
            cur = []
            cur.append(accounts[i][0])
            for email in sets[j]:
                cur.append(email)
            ret.append(cur)
    return ret