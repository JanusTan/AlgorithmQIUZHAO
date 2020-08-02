# 121. 买卖股票的最佳时机
# 时间复杂度O(n)，空间复杂度O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(price, minprice)
            maxprofit = max(maxprofit, price - minprice) # 动态规划的思想，根据以前的结果对当前进行选择，有回退功能
        return maxprofit