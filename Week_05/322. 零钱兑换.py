class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = 1,2,5. F[i]表示组成i最少的硬币个数。
        # F(0)	0 //金额为0不能由硬币组成
        # F(1)	1 //F(1)=min(F(1−1),F(1−2),F(1−5))+1=1
        # F(2)	1 //F(2)=min(F(2−1),F(2−2),F(2−5))+1=1
        # F(3)	2 //F(3)=min(F(3−1),F(3−2),F(3−5))+1=2
        # F(4)	2 //F(4)=min(F(4−1),F(4−2),F(4−5))+1=2
        # ...	...
        # F(11)	3 //F(11)=min(F(11−1),F(11−2),F(11−5))+1=3
        # dp方程：dp[i] = min(dp[i-coins[:]]) + 1。由组成i-coins[i]的最少硬币数加上一个硬币组成
        # 想去掉F（<0）,必须i-coins>=0
        if not coins or amount<0: return -1
        if amount==0: return 0 # 当数目是0时，输出应该是0，这个容易忘
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1