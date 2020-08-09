# dp[i][j] = 表示已（i,j)为坐标的格子，作为正方形的右下角的最大的边
# dp公式是去上，左，左上最小的dp加上1,得到面积的边
# 边界值：i或j等于0时，最大只能是1即dp[i][j] = 1

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 找最大面积，即往DP方向的思路。
        # 1. 子问题：dp[i][j] = 表示已（i,j)为坐标的格子，作为正方形的右下角的最大的边
        # 2. DP状态定义：dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1 # 上面、左边、左上
        # 3. DP方程：
        # 4. 边界：i==0 or j==0: dp[i][j] = 1
        if not matrix:
            return 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0]* columns for _ in range(rows)] # 生成rows x columns
        max_sides = 0
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i==0 or j==0: dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                max_sides = max(max_sides, dp[i][j])
        return max_sides*max_sides
