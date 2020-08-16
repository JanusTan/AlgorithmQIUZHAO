class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 在第一题基础上判断格子（i,j）上是否有障碍，无才进行DP方程。初始化一旦遇到障碍物后面dp的都是0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # if obstacleGrid[0][0] ==1: return 0
        if m<=0 or n<=0:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1
        for t in range(1,m):
            for k in range(1,n):
                if obstacleGrid[t][k] == 0:
                    dp[t][k] = dp[t-1][k] + dp[t][k-1]
        return dp[-1][-1]