# 121. 买卖股票的最佳时机
# 时间复杂度O(n)，空间复杂度O(1)
# 状态定义：只允许一笔交易，确保当前dp[i]的利润是最大的，则dp[-1]为结果
# 状态方程： dp[i] = max(dp[i-1], price - minprice) # 只允许一笔交易
# 空间复杂度降低： 只要一个变量maxprofit就可代替dp[i]和dp[i-1],其他dp里的元素不需要存储

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(price, minprice)
            maxprofit = max(maxprofit, price - minprice) # 动态规划的思想，根据以前的结果对当前进行选择，有回退功能
        return maxprofit

        # k=1。当前没持有股票,则最大利润在：1. 前一天持有股票，但今天卖出了 2. 前一天没股票，但今天也没买。两者中最大的利润产生. 当前持股情况下则最大利润在：1. 前一天持有股票，今天没卖出了 2. 前一天没持股票，但今天买入了。两者中最大的利润产生.
        # dp[i][k][0] = max(dp[i-1][k][1]+price, dp[i-1][k][0])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price)
        # k=1,对这个DP方程没有影响。所以：
        # dp[i][0] = max(dp[i-1][1]+price, dp[i-1][0])
        # dp[i][1] = max(dp[i-1][1],  - price) # dp[i-1][0][0]=0因为没有购买次数
        # 初始值dp[i-1]当i=0会出现dp[-1]，都跳过。
        # 优化： 只涉及到dp[i][0]-dp[i-1][0]和dp[i][1]-dp[i-1][1]，且这两相邻，所以可以用两个变量
        # dp_i_0 = 0  # dp[-1][0]=0
        # dp_i_1 = -float('inf')  # dp[-1][1]不存在取负无穷
        # for price in prices:
        #     dp_i_0 = max(dp_i_1 + price, dp_i_0)
        #     dp_i_1 = max(dp_i_1, -price)
        # return dp_i_0  # 最后一天没有持股剩下时为最大利润