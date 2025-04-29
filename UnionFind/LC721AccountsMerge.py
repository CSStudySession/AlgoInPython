from typing import List
import collections
'''
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
    email_to_names = collections.defaultdict(list)
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
    user_group = collections.defaultdict(list)
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
print(id_merge(accounts))


# 原题. 思路:并查集 
def find(union: List[int], id: int) -> int:
    if union[id] != id: # 根不是自己: 递归寻根并把自己挂在一级根上(路径压缩)
        union[id] = find(union, union[id])
    return union[id]

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    len_accnt = len(accounts)
    union = []
    for i in range(len_accnt): # 初始化union-find:每个account都以自己为根
        union.append(i)
    
    # 记录每个邮箱在哪些id下出现过 构建{email:[ids]}索引
    email_to_ids = collections.defaultdict(List)
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