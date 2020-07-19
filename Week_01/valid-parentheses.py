# 20. 有效的括号
# 要遍历整个字符串，时间复杂度O（n）。空间O（n)因为要创建一个栈和字典


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        dic1 = {'(':')', '[':']','{':'}','-1':'-1'}
        stack=['-1']
        for char in s:
            if char in dic1:
                stack.append(char)
            elif char != dic1[stack.pop()]:
                return False
        return len(stack)==1

