class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 2 的幂次方的二进制应该只有1个1
        # 题目说是整数，有可能是0，所以要同时判断是否为负整数或者0
        return n>0 and (n&(n-1) == 0)