class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        dic ={}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        for key in dic:
            if dic[key] == 1: return s.index(key)
        return -1
