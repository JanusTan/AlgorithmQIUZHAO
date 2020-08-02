# 78. 子集
# 时间复杂度O(2^n)要生成所有子集， 空间复杂度O(2^n)，递归的函数会调用栈空间


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                helper(j+1, temp+[nums[j]]) # 注意[1,2,3]+[4,5] = [1,2,3,4,5], nums[j]是一个整数[nums[j]]才是list
        helper(0, [])
        return res