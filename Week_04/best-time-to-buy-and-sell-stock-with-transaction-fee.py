# 714. 买卖股票的最佳时机含手续费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 只交一次手续费，即买入的时候减去股钱和手续费
        dp_0 = 0
        dp_1 =  - float('inf')
        for price in prices:
            dp_0 = max(dp_0, dp_1 + price)
            dp_1 = max(dp_1, dp_0 - fee - price)
        return dp_0