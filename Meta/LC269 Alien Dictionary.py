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

followup: 如果input 不valid怎么办?需要figure out什么是不valid的input.
invaid input: can't construct an order of chars.
1. 相邻词 后一个词是前一个的前缀 且前一个词更长. 'abc', 'ab' 任何基于字典序的order 短的应该排在长的前面
2. there's cycle. 'z', 'x', 'z' --> z < x, and z > x. 有环 无法排序
'''
def alienOrder(words: list[str]) -> str:
    if not words:
        return ''
    
    graph = collections.defaultdict(set) # 邻接表建图
    for word in words: # 每个节点初始化(neighbor都是空set)
        for ch in word:
            if ch not in graph:
                graph[ch] = set()
    
    for i in range(len(words) - 1): # 每次取出相邻两个词 逐字符对比 推导顺序 更新graph edges
        word, next_word = words[i], words[i + 1]
        length = min(len(word), len(next_word))
        j = 0
        has_diff = False # 判断相邻两个词的最长前缀是否有diff 如果无 且前面词比后面长 则输入不合法
        while j < length:
            if word[j] != next_word[j]:
                graph[word[j]].add(next_word[j])
                has_diff = True
                break # 找到第一个diff就要break 之后的顺序无法推导
            j += 1
        if not has_diff and len(word) > len(next_word): # 输入不合法
            return ''
    
    in_degree = {ch: 0 for ch in graph} # 初始化每个节点入度为0
    for nbrs in graph.values():
        for ch in nbrs:
            in_degree[ch] += 1
    # 用queue拓扑排序
    queue = collections.deque()
    for ch in in_degree: # 入度为0的点入队
        if in_degree[ch] == 0:
            queue.append(ch)
    ret = [] # 结果集
    while queue:
        ch = queue.popleft()
        ret.append(ch)
        for nbr in graph[ch]: # 当前点的邻居入度均-1 再看其入度是否为0 0就入队
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    return ''.join(ret) if len(ret) == len(graph) else ''

# variant: 不用输出任何不确定顺序的字母
# 思路:拓扑排序 核心是排除图中的孤立点(nodes without any edge connections)
# 1. 构造graph时 只通过前后单词对比构造图 不每个节点先初始化一个空邻居set
# 2. 构造in_degree时 只通过graph的出边关系 不初始化每个节点入度为0
def alienOrder_no_singulars(words: list[str]) -> str:
    if not words:
        return ''
    
    graph = collections.defaultdict(set) # 邻接表建图 这里不初始化每个节点的邻居set
    
    for i in range(len(words) - 1): # 每次取出相邻两个词 逐字符对比 推导顺序 更新graph edges
        word, next_word = words[i], words[i + 1]
        length = min(len(word), len(next_word))
        j = 0
        has_diff = False # 判断相邻两个词的最长前缀是否有diff 如果无 且前面词比后面长 则输入不合法
        while j < length:
            if word[j] != next_word[j]: # 只有明确顺序关系的字母才加入图
                graph[word[j]].add(next_word[j])
                has_diff = True
                break # 找到第一个diff就要break 之后的顺序无法推导
            j += 1
        if not has_diff and len(word) > len(next_word): # 输入不合法
            return ''
    
    in_degree = collections.defaultdict(int) # 入度dict 不初始化每个key为0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        if u not in in_degree: # 对于有边关系的 入度为0的点 才更新in_degree 排除孤立点
            in_degree[u] = 0
    # 用queue拓扑排序
    queue = collections.deque()
    for ch in in_degree: # 入度为0的点入队
        if in_degree[ch] == 0:
            queue.append(ch)
    ret = [] # 结果集
    while queue:
        ch = queue.popleft()
        ret.append(ch)
        for nbr in graph[ch]: # 当前点的邻居入度均-1 再看其入度是否为0 0就入队
            in_degree[nbr] -= 1
            if in_degree[nbr] == 0:
                queue.append(nbr)
    # 只返回有明确edge关系的字母 即参与拓扑排序的
    return ''.join(ret) if len(ret) == len(in_degree) else ''