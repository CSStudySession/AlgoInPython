import collections
'''
思路:拓扑排序
1.构建图
遍历所有单词 将出现过的字母都加入图中 初始化每个字母的邻居集合set()
2.建立字母之间的先后关系
对于相邻的两个单词word1和word2 找出它们第一个不同的字母c1和c2 可以推出c1应该排在c2前面
即添加有向边 c1 -> c2。
  -- 如果word1比word2长 且word1是以word2为前缀:如["abc", "ab"] 不合法 直接返回 ""。
3.计算每个字母的入度 in-degree
对每条边 a -> b 将b的入度加一. 将所有入度为0的字母加入队列中 准备进行拓扑排序
4.拓扑排序 BFS
每次从队列中取出一个入度为0的字母 将它加入结果中
遍历它所有的邻居字母，更新邻居的入度，如果变成 0 则也加入队列
如果最后拓扑排序的结果长度和图中节点数不一致 说明有环 返回 ""
let n is num of words, k is num of letters(26 at most), E is num of edges between letters
T(n*L) for build graph, L is avg len of word, T(k+E) for topo sort. 
so TC is (n*L+k+E) S(k+E): for graph 最多k个节点 每个节点最多指向其他K-1个点(num of edges)
'''
def alienOrder(words: list[str]) -> str:
    if not words:
        return ''
    
    graph = collections.defaultdict(set)
    for word in words:
        for ch in word:
            if ch not in graph:
                graph[ch] = set()
    
    for i in range(len(words) - 1):
        word, next_word = words[i], words[i + 1]
        length = min(len(word), len(next_word))
        j = 0
        has_diff = False
        while j < length:
            if word[j] != next_word[j]:
                graph[word[j]].add(next_word[j])
                has_diff = True
                break
            j += 1
        if not has_diff and len(word) > len(next_word):
            return ''
    
    in_degree = {ch: 0 for ch in graph}
    for nbrs in graph.values():
        for ch in nbrs:
            in_degree[ch] += 1
    queue = collections.deque()
    for ch in in_degree:
        if in_degree[ch] == 0:
            queue.append(ch)
    ret = []
    while queue:
        ch = queue.popleft()
        ret.append(ch)
        for nbr in graph[ch]:
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    return ''.join(ret) if len(ret) == len(graph) else ''