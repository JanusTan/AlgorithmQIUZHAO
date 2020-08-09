# 122. 买卖股票的最佳时机 II
# 时间复杂度O(n)，空间复杂度O(1)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            temp = prices[i] - prices[i-1] # 计算是否是上涨日，上涨日都买入，下涨日跳过，则得到最大的利润
            if temp > 0: # 贪心思想，子问题的最优解能递推到最终问题的最优解，不能回退
                profit += temp
        return profit
    # analyze:
    # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+price)
    # dp[i][k][1] = max(dp[i-1][k-1][0] - price, dp[i-1][k][1])
    # k = +inf, k-1=+inf
    # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price)
    # dp[i][1] = max(dp[i-1][0] - price, dp[i-1][1])
    # dp[i][0], dp[i-1][0]和dp[i][1]，dp[i-1][1]
    # dp[i-1]初始化
    # coding:
    # d_i_0 = 0
    # d_i_1 = - float('inf')
    # for price in prices:
    #     d_i_0 = max(d_i_0, d_i_1 + price)
    #     d_i_1 = max(d_i_1, d_i_0 - price)
    # return d_i_0