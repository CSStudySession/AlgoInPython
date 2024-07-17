from typing import List
import collections
class Solution:
    def find(self, union: List[int], id: int) -> int:
        if union[id] != id: # 根不是自己: 递归寻根并把自己挂在一级根上(路径压缩)
            union[id] = self.find(union, union[id])
        return union[id]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
                union[self.find(id_list[k])] = self.find(id_list[0])

        # 把邮箱按照其在 u-f处理后的id所属的集合 加入到同一个set中
        sets = [set()] * len_accnt # [set1, set2, ...]
        for i in range(len_accnt):
            for j in range(1, len(accounts[i])):
                sets[self.find(i)].add(accounts[i][j])

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