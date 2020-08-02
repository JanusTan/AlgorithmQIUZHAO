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