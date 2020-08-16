class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def add_parentthesis(left, right, s, result):
            # terminator
            if left+right >= 2*n:
                result.append(s)
                return
            # current level and drill down这里有剪枝的思想
            if left<n:
                add_parentthesis(left+1, right, s+"(", result)
            if right < left:
                add_parentthesis(left, right+1, s+")", result)
        if n==0: return []
        left, right = 0, 0
        result, s = [], ""
        add_parentthesis(left, right, s, result)
        return result