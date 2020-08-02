# 153. 寻找旋转排序数组中的最小值
# 时间复杂度O(logn)， 空间复杂度O(1)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        left = 0
        right = len(nums) -1
        while left < right:
            mid  = left + (right - left) // 2
            if nums[mid] < nums[right]: # 中值比右边的小，缩小右半圈
                right = mid
            elif nums[mid] > nums[right]: # 中值比右边大，缩小左半圈
                left = mid + 1
        return nums[left]