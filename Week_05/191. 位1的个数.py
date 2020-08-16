class Solution:
    def hammingWeight(self, n: int) -> int:
        # n&(n-1)弹出最低位的1
        result = 0
        while (n != 0):
            n=n&(n-1)
            result +=1
        return result