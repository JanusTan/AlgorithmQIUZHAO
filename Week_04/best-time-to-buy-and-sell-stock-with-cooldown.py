# 309. 最佳买卖股票时机含冷冻期
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # k=+inf, k在DP里没作用所以降到二维,卖出后要隔一天才能买
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k-1][0] - prices[i])# 卖出后要隔一天才能买dp[i-2]
        # 三个变量可存储完dp_0, dp_1, dp_prev_0
        dp_0 = 0
        dp_1 = -float('inf')
        dp_prev_0 = 0 #存dp[i-2][0]
        for price in prices:
            temp = dp_0
            dp_0 = max(dp_0, dp_1 + price)
            dp_1 = max(dp_1, dp_prev_0 - price)
            dp_prev_0 = temp
        return dp_0

