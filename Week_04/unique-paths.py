# 62. 不同路径
# 时间复杂度O(m*n)，空间复杂度O(m*n)
# 1. 定义的状态：dp[i][j]代表的是走到（i,j）可能的路径数
# 2. 建立递推方程：走到当前格子的路径总和是，格子左边的格子的路径总和 + 格子上边的格子的路径总和，即dp[i][j] = dp[i][j-1] + dp[i-1][j]
# 3. 设定初始值。递推方程i,j下边要从1开始，也就是格子最左边和最上边的格子设置为1, 即初始化为的d[i][0] = 1, d[0][j] = 1


def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        d[i][0] = 1
    for j in range(n):
        d[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]
