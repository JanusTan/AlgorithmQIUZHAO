class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        temp = s.split()
        temp.reverse()
        return " ".join(temp)
