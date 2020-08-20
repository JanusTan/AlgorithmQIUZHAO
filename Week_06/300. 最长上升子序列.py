class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 定义状态： dp[i]表示s[0],s[1]...s[i-1]组成的序列的最长的上升序列长度
        # DP方程： 遍历dp[i]之前的每个数字，如果出现小于s[i]的，dp[i] = max(dp[i],dp[j] + 1)
        # 初始化和边界： dp一维数组全初始化为1, dp[0] = 1
        if not nums: return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)