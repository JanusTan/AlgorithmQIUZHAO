# 剑指 Offer 11. 旋转数组的最小数字
# 时间复杂度O（logn）, 空间O（1）


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i = 0
        j = len(numbers) - 1
        while i<j:
            m = (i+j)//2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j=m
            else:
                j -= 1
        return numbers[i]