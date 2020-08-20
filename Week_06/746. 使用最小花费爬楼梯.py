class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 画一个三阶梯图，第一阶梯为i-1阶梯，第二阶梯为i阶梯，第三阶梯为i阶梯的顶层
        # dp[i]表示走到i阶梯的顶层要花费的最少体力：有两种可能取其最小，第一种从i层一步到其顶层。第二种从
        # i-1层跨两步到i的顶层。已知i层是i-1层的顶层即dp[i-1],在这个基础加上i这层体力可以一步到i的顶层
        if not cost: return 0
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = 0
        dp[1] = min(cost[0], cost[1])
        for i in range(2,n):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i-1])
        return dp[-1]