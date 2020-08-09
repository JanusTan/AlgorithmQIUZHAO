class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+price)
    # dp[i][k][1] = max(dp[i-1][k-1][0] - price, dp[i-1][k][1])
    # k =2, 2对DP，分别是k=1的，k=2的
    # k=1
    # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+price)
    # dp[i][1][1] = max( - price, dp[i-1][1][0])
    # k=2
    # dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1]+price)
    # dp[i][2][1] = max(dp[i-1][1][0] - price, dp[i-1][2][0])
    # 初始值： dp[-1][1][0] = 0， dp[-1][1][1] = -inf, dp[-1][2][0] = 0， dp[-1][2][1] = -inf,
    # 简化：四个变量即可表示万DP方程中的dp变量dp_1_0, dp_1_1, dp_2_0, dp_2_1
        dp_1_0, dp_1_1, dp_2_0, dp_2_1 = 0, -float('inf'),0, -float('inf')
        for price in prices:
            dp_2_0 = max(dp_2_0, dp_2_1+price)
            dp_2_1 = max(dp_1_0 - price, dp_2_1)
            dp_1_0 = max(dp_1_0, dp_1_1 + price)
            dp_1_1 = max(-price, dp_1_1)
        return dp_2_0


