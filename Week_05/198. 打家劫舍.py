class Solution:
    def rob(self, nums: List[int]) -> int:
        # 状态定义： dp[i]表示偷[0,1..,i]能得到的最大金额，结果为dp[n]
        # dp方程： dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # 初始值和边界：dp[i-2]， i从2开始，那么dp[1]为nums[0],dp[0]为1
        n = len(nums)
        if n==0: return 0
        if n==2: return max(nums[1],nums[0])
        if n==1: return nums[0]
        dp = [0 for _ in range(n)] # n个dp状态
        dp[0] =nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,n): # n-1个
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    # dp0 = nums[0]
    # dpi = max(nums[1], nums[0])
    # for i in range(2, n):  # n-1个
    #     temp = dpi
    #     dpi = max(dpi, dp0 + nums[i])
    #     dp0 = temp
    # return dpi