# 647. 回文子串
#
# 回文子串：字符串倒过来读也和原来一样，如level
# dp[i][j]表示s[i:j+1]是否为回文子串, 两个状态True和False
# dp[i][j]由dp[i+1][j-1]决定，如s=babad(i指向b,j指向d时)
# 特殊情况s=cbbd(i,j都指向两个b,即j-1=1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if not s or s[0] == "":
            return 0
        result = n
        dp = [[0] * n for _ in range(n)]
        for k in range(n): dp[k][k] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):  # 右下角开始算，因为要用到dp[i+1]
                if s[i] == s[j]:  # DP方程
                    if j - i == 1:  # ij左右相邻特殊情况
                        dp[i][j] = 1
                    else:  # DP方程1
                        dp[i][j] = dp[i + 1][j - 1]
                else:  # DP方程2
                    dp[i][j] = 0

                if dp[i][j] == 1:
                    result += 1

        return result

