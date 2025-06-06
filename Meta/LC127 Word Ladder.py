import collections
'''
思路:BFS 要找最短路径 可以将这个问题建模为一个图的问题：
- 每个单词是一个节点
- 若两个单词只差一个字母，则它们之间有一条边
- 问题就转化为 在这个图中 从beginWord到endWord的最短路径长度

设L为单词的长度 N为len(word_list) T(NL*26)=T(NL)  S(N+L) from visited, queue, next_word
'''
def ladderLength(begin_word: str, end_word: str, word_list: list[str]) -> int:
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    queue = collections.deque([(begin_word, 1)]) # 把step和单词包在一起入队
    visited = set([begin_word]) # 这里要用[]包起来 当成一个整体 否则变成独立字母在set里
    while queue:
        cur, step = queue.popleft() # 这里是popleft()
        if cur == end_word:
            return step
        for next_word in get_next_words(cur, word_set):
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, step + 1))
    return 0

def get_next_words(word, word_set):
    next_words = []
    for i in range(len(word)):
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if word[i] == ch:
                continue
            new_word = word[:i] + ch + word[i+1:]
            if new_word in word_set: # 新词要在字典里出现过
                next_words.append(new_word)
    return next_words