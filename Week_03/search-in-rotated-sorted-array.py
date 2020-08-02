# 33. 搜索旋转排序数组
# 时间复杂度O(logn)，空间复杂度O(1)，二分查找


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right= len(nums) - 1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]: # 右边有序
                if nums[mid] < target <= nums[right]: # target在这一段序列
                    left = mid + 1
                else:
                    right = mid - 1
            else: # 左边有序
                if nums[left] <= target < nums[mid]: # 在左段序列
                    right = mid -1
                else:
                    left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1