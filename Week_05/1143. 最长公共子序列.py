class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 定义状态dp[i][j]表示test1[1:i], test2[1:j]最长的公共子序列,为了方便dp递推dp[i-1][j-1]的状态, 返回dp[-1][-1]
        # 定义DP方程，当是text1[i-1] = text2[j-1]时，dp[i][j] = dp[i-1][j-1] + 1, 否则取当前dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # 边界和初始化：dp[i][0]和dp[0][j]都取0
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]  # 定义一个mxn矩阵存储dp状态
        for i in range(1,m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]