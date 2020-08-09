# 127. 单词接龙
# 时间复杂度O(N*M), 空间复杂度O(n)


def ladderLength(beginWord, endWord, wordList):
    from collections import deque
    queue = deque([[beginWord, 1]])
    word_list = set(wordList) # O(N)
    while queue: # N: 候选单词的平均个数
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)): # O(M)单词平均长度
            for c in 'abcdefghijklmnopqrstuvwxyz': #O(1)
                new_word = word[:i] + c + word[i + 1:]
                if new_word in word_list:
                    word_list.remove(new_word)
                    queue.append([new_word, length + 1])
    return 0
