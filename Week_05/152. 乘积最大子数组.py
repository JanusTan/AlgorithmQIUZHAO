class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 因为有负数的存在，会使得最大的变最小，最小的变最大，所以还需要维护另外一个状态opt[j]，来存最小的。当负数出现时交换最大的和最小的
        n = len(nums)
        if n==0:
            return 0
        dp = [0 for _ in range(n)]
        opt = [0 for _ in range(n)]
        dp[0],opt[0], result = nums[0], nums[0],nums[0]
        for i in range(1,n):
            if nums[i]<0: dp[i-1],opt[i-1] = opt[i-1],dp[i-1]
            dp[i] = max(dp[i-1]*nums[i], nums[i])
            opt[i] = min(opt[i-1]*nums[i],nums[i])
            if result<dp[i]: result = dp[i]
        return result