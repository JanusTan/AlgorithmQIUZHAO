class Solution:
    def reverseBits(self, n: int) -> int:
        # range(31,-1,-1)从低位开始遍历
        # (n>>(31-i)) & 1 取出31-i位上的数，是1还是0
        # << i 挪到翻转后的位置
        # result| 设置第i位的数
        result = 0
        for i in range(31, -1, -1):
            result = result | (((n >> (31 - i)) & 1) << i)
        return result
