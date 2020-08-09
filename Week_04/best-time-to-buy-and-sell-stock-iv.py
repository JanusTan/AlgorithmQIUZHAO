# 188. 买卖股票的最佳时机 IV
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1] + price)
        # dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0] - price)
        # k > len(prices)/2，相当于不限次数了，即k=+inf的情况
        # dp[-1]的情况：dp[-1][k][0] = 0, dp[-1][k][1] = -inf的情况
        n = len(prices)
        def max_k_inf_profit(prices):
            d_i_0 = 0
            d_i_1 = -float('inf')
            for price in prices:
                d_i_0 = max(d_i_0, d_i_1 + price)
                d_i_1 = max(d_i_1, d_i_0 - price)
            return d_i_0
        if k >n/2:
            return max_k_inf_profit(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)] # ixkx2
        for i in range(n):
            for j in range(k,0,-1): # k最后只能取到1。式子2，k-1情况:dp[i][0][0]第i天允许最大交易0次，不持股，则最大利润为0
                if i==0: # dp[-1]
                   dp[0][j][0] = 0
                   dp[0][j][1] = -prices[i] #dp[0][k][1]表示第一天买了
                   continue
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]