# 15. 三数之和
# 讲出三种解法及其时间复杂度即可得到special offer hire
# 该函数时间复杂度, 遍历数组双指针O(n)*O(n)=O(n^2)
# 空间复杂度： 只开了一个数组存有限个解集，所以是O(n)
# 做题记录


def threeSum2(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):  # 只遍历到倒数第三个range(len(nums) - 2)，len(nums) - 2取不到的
        if i > 0 and nums[i] == nums[i - 1]:  # 因为排过序，所以需要去掉那些重复的目标
            continue
        l, r = i + 1, len(nums) - 1  # 分配左右指针
        while l < r:  # 去掉重复的解
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1;
                r -= 1
    return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set() # 集合会去掉重复的子集（重复的子集是指每个维度都相同）
        for i, v in enumerate(nums):
            self.twoSum(nums[i + 1:], -v, ans)
        return list(ans) # set转list

    def twoSum(self, nums, target, ans):
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                ans.add((v, target - v, -target)) # set的添加子集
            d[v] = i


a = [0, 0, 0]
a2 = [0, 0, 0, 0, 0]
a1 = [-1, 0, 1, 2, -1, -4]
print(threeSum2(a1))
