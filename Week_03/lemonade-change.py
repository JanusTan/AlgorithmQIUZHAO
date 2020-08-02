# 860. 柠檬水找零
# 时间复杂度O(n)，空间复杂度O(1)


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten  = 0, 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five, ten  = five -1, ten + 1
            elif i==20 and ten>0: five, ten  = five -1, ten - 1
            else: five -= 3
            if five < 0: return False
        return True