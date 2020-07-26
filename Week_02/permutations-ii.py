# 47. 全排列 II
# 时间复杂度O(n), 空间复杂度O(n)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(cur_nums, nums):
            if not nums:
                ans.append(cur_nums)
            else:
                for i, num in enumerate(nums):
                    if i>=1 and nums[i] == nums[i-1]:
                        continue
                    helper(cur_nums+[num], nums[:i]+nums[i+1:])
        ans = []
        nums = sorted(nums)
        helper([],nums)
        return ans