# 127. 单词接龙
# 时间复杂度O(26*wordlenth), 空间复杂度O(n)


def ladderLength(beginWord, endWord, wordList):
    from collections import deque
    queue = deque([[beginWord, 1]])
    word_list = set(wordList)
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in word_list:
                    word_list.remove(new_word)
                    queue.append([new_word, length + 1])
    return 0
