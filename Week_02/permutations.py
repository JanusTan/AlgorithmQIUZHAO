# 46. 全排列
# 时间复杂度O(n),递归的深度为nums的长度, 空间复杂度O(n)，一个一维数组被开了


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(cur_nums, nums):
            if not nums:
                ans.append(cur_nums)
            else:
                for i, num in enumerate(nums):  # 每次都遍历整个数组，然后把当前遍历的加到已有的序列，剩下的留到下一个递归
                    helper(cur_nums+[num], nums[:i]+nums[i+1:])
        ans = []
        helper([], nums)
        return ans