class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 状态定义：dp[i]表示以当前下标结尾的最大连续子数组之和，结果返回一个存储最大连续子数组之和的变量max
        # dp方程：dp[i] = max(dp[i-1]+nums[i], nums[i])
        # 边界和初始值：dp[i-1]，即dp[0] = nums[0]
        # 优化空间复杂度：dp[i] = max(dp[i-1]+nums[i], nums[i])，dp_i = max(dp_i+nums[i], nums[i])
        n = len(nums)
        if n == 0:
            return 0
        # dp = [0 for _ in range(n)]
        # result, dp[0] = nums[0], nums[0]
        # for i in range(1,n):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        #     if result < dp[i]: result=dp[i]
        # return result

        result, dp_i = nums[0], nums[0]
        for i in range(1, n):
            dp_i = max(dp_i + nums[i], nums[i])
            if result < dp_i: result = dp_i
        return result
