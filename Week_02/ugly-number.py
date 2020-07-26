# 263. 丑数
# 时间复杂度O(n), 空间复杂度O(1)


class Solution:
    def isUgly(self, num: int) -> bool:
        # terminater
        if num == 1:
            return True
        if num < 1:
            return False
        # cur level
        if num%2 == 0:
            num = num // 2
        elif num%3 == 0:
            num = num//3
        elif num%5 == 0:
            num = num//5
        else:
            return False
        #drill
        # reserve
        return self.isUgly(num)