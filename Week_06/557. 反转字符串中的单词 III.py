class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        list1 = s.split()  # ['abc','kls']
        result = []
        for l in list1:
            result.append("".join(reversed(l)))
        return " ".join(result)
