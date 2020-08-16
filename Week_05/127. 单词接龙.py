class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import string
        # set查询时间复杂度是O（1）
        word_list = set(wordList)
        # BFS tempalte
        queue = [[beginWord, 1]]
        while queue:
            word, length = queue.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_list:
                        word_list.remove(new_word)
                        queue.append([new_word,length+1])
        return 0