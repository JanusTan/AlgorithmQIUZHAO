class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i],走i个阶梯可用的方法
        # dp[i] = dp[i-1] + dp[i-2]
        # dp[i-2],i从3开始，dp0=0,dp1=1,dp2=2, 当n<=2，返回n
        if n<=2: return n
        dp = [0 for _ in range(n+1)]
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]