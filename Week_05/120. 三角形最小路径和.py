class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 状态定义：dp[i][j]表示当前（i,j）到最后一层的最小路径,自底向上递推
        # dp方程：dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        # 初始化和边界：最后一层的dp都是0，在dp初始化时完成
        # dp方程简化：式子中的三个变量，统一用dp[j]表示 dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        row = len(triangle)
        if not triangle or triangle[0] == []:
            return 0
        # dp = [[0]*(row+1) for _ in range(row+1)] # (row+1)x(row+1)矩阵存储dp,因为自底向上推的时候算三角最后一行dp[i+1]希望是自身
        # for i in range(row-1,-1,-1):
        #     for j in range(0,i+1):
        #         dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        # return dp[0][0]

        dp = [0 for _ in range(row+1)]
        for i in range(row-1, -1, -1):
            for j in range(0,i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[j]