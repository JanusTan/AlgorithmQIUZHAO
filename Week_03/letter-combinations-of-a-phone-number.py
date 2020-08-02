# 17. 电话号码的字母组合
# 时间复杂度O(n)，递归树的深度，空间复杂度O(n)，开了一个数组


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}

        def backtracking(sub_combine, next_digit):
            if len(next_digit) == 0:
                result.append(sub_combine)
            else:
                for char in dic[next_digit[0]]:
                    backtracking(sub_combine + char, next_digit[1:])

        result = []
        backtracking('', digits)
        return result
