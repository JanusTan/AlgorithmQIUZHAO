# 32. 最长有效括号
# 时间复杂度O(n), 空间复杂度O(n)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or s[0] == "":
            return 0
        stack = []
        result = 0
        for i in range(len(s)):
            if not stack or s[i] == "(" or s[stack[-1]] == ")": # 入栈条件， 栈空，左括号，栈顶是右括号
                stack.append(i)
            else:
                stack.pop()
                result = max(result, i-(stack[-1] if stack else -1)) # i - stack[-1]合法括号
        return result