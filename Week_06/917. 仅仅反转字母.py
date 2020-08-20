import string
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # 注意：string的对象不能够赋值修改，最好转换成list
        letters = []
        no_letters_idx = []
        list_S =list(S)
        if not S: return S
        # 提取出只含字母的字符串，翻转
        # 当遇到字母，依次覆盖整个字符串的每一位
        for  char in S:
            if char in string.ascii_letters: letters.append(char)
        letters.reverse()
        for i,char1 in enumerate(S):
            if char1 in string.ascii_letters: list_S[i] = letters.pop(0)
            else: continue
        return "".join(list_S)
