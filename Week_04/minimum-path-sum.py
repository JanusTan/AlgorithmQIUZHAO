# 64. 最小路径和
# 时间复杂度O(mxn)，空间复杂度O(1)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DP方程：想要走到(i,j)的路径和最短，dp[i][j]是左边或上方边的最小路径值加上当前的数字
        # 由于grid只会更改一次，所以可以替代dp数组节省空间复杂度
        for i in range(len(grid)): # row
            for j in range(len(grid[0])): # column
                if i==j==0: continue # gid[0][0]=grid[0][0]
                elif i==0: # 边界1，最短路径只能从左边来[i][j-1]
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j==0: # 边界1，最短路径只能从上边来[i-1][j]
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]