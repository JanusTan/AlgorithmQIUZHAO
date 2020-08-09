# 91. 解码方法
# 时间复杂度O(n)，空间复杂度O(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        # 定义状态： dp[i]表示s[:i]这一段的解码方法总和，注意此时只能取到s[i-1]，因此结果应该是求dp[i+1]，即s[:i+1]整段的解码
        #           方法的总和
        # 状态方程：初始化：dp[i+1]下标从1开始。dp[0]定义为0
        #            计算dp[i+1]，可以由这两部分组成：当s[i]是1-9的数，则s[:i+1]的解码方法即dp[i+1]为s[:i]的解码方法dp[i]
        #            ；当s[i-1]s[i]组成的两数字在10-26之间，则s[:i+1]的解码方法即dp[i+1]为s[:i-1]的解码方法dp[i-1]组成
        #             两条件都满足，则为dp[i+1] = dp[i] + dp[i-1]
        # 因为题目说了s非空，所以不用判断长度了
        dp=[1,0]
        dp[0+1] = 1 if s[0] !='0' else 0
        for i in range(1,len(s)):
            dp.append(0)
            if s[i] !='0':
                dp[i+1] += dp[i]
            if '10' <= s[i-1:i+1] <= '26':
                dp[i+1] = dp[i+1] + dp[i-1] # i=1时，此处结果应为》=1，所以dp[0]=1初始化
        return dp[-1]

    # 可以优化，因为dp[-3]之前的状态没必要储存了优化到O(1)
    #     dp = [1, 0]
    #     dp[0 + 1] = 1 if s[0] != '0' else 0
    #     for i in range(1, len(s)):
    #         dp.append(0)
    #         if s[i] != '0':
    #             dp[-1] += dp[-2]
    #         if '10' <= s[i - 1:i + 1] <= '26':
    #             dp[-1] = dp[-1] + dp[-3]  # i=1时，此处结果应为》=1，所以dp[0]=1初始化
    #         dp.pop(0)
    #     return dp[-1]