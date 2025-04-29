'''
将句子中的每个单词用如下规则转换:
- 以元音开头 → 直接加 "ma"。
- 以辅音开头 → 把首字母移到词尾，再加 "ma"。
- 每个单词再加上对应数量的 "a": 第1个单词加1个 第二个加2个 以此类推
最后把所有单词拼接为一个句子返回。

T(n^2) S(n^2)
'''
def toGoatLatin(S: str) -> str:
    words = S.split()     # 将句子按空格拆分为单词列表
    result = []           # 用于保存转换后的每个单词

    for i in range(len(words)):
        word = words[i]
        index = i + 1     # 单词索引从1开始

        # 判断是否以元音字母开头（大小写都考虑）
        if word[0] in 'aeiouAEIOU':
            new_word = word
        else:
            # 如果是辅音开头，把第一个字母移到词尾
            new_word = word[1:] + word[0]

        new_word += 'ma'          # 添加“ma”后缀
        new_word += 'a' * index   # 根据索引添加相应数量的“a”

        result.append(new_word)  # 添加到结果列表中
    return ' '.join(result)      # 将所有单词拼接为最终句子

