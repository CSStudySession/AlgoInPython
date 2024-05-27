from typing import List

class Solution:
    # method 1: DFS graph
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        graph = collections.defaultdict(set)
        emailToName = {}
     
        # build undirected graph with emails: email1 <-> sets of other emails. 
        # email1作为root email, other email只需要加email1即可(不需要完全双向 只需要联通即可)
        for account in accounts:    
            email1 = account[1]
            emailToName[email1] = account[0]    
            for i in range(2, len(account)):  
                graph[email1].add(account[i])
                graph[account[i]].add(email1)

        visited = set() # this is global visited.
        
        res = [] #res是list of tmp. tmp是每个account的搜索结果
        for account in accounts:
            email1 = account[1]
            if email1 not in visited:
                tmp = [] # 对每个account都需要一个tmp. 结构是: ["name", "email1", "email2""] 
                visited.add(email1)
                tmp.append(account[0])
                tmp.append(email1)
            
                self.dfs(email1, graph, tmp, visited) #以email1为起始点 search for all connected emails, add to tmp
                tmp[1:] = sorted(tmp[1:])
                res.append(tmp)
        return res

    def dfs(self, node, graph, tmp, visited):
        if node not in graph:
            return 

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                tmp.append(nei)
                self.dfs(nei, graph, tmp, visited)