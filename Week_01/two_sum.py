# 1. 两数之和
# 排序O(nlogn), 双指针O(n), 删除O(n), 所以是O(nlogn)
# 只有创建了一个数组sorted_nums所以是O(n)


# def twoSum(nums, target):
#     len1 = len(nums)
#     if len1 < 2:
#         return []
#     # 排序，双指针
#     sorted_nums = sorted(nums)
#     L = 0
#     R = len1 - 1
#     while L < R:
#         if target == sorted_nums[L] + sorted_nums[R]:
#             break
#         elif sorted_nums[L] + sorted_nums[R] < target:
#             L += 1
#         elif sorted_nums[L] + sorted_nums[R] > target:
#             R -= 1
#     idx1 = nums.index(sorted_nums[L])
#     nums.pop(idx1)
#     idx2 = nums.index(sorted_nums[R])
#     if idx2 >= idx1:
#         idx2 += 1
#     return [idx1, idx2]

# 方法二：hash, 时间复杂度O（n）,空间复杂度O（n）

def twoSum(nums, target):
    hashset = {}
    for i in range(len(nums)):
        if hashset.get(target - nums[i]) is not None:
            return [hashset.get(target - nums[i]), i]
        hashset[nums[i]] = i


# def twoSum(nums, target):
#     dic={}
#     for k,v in enumerate(nums):
#         if target-v in dic: #写之前判断，避免了重复元素的覆盖
#             return [dic[target-v],k]
#         dic[v]=k


# nums, target = [2, 7, 11, 15], 9
nums, target = [3, 2, 3], 6
print(twoSum(nums, target))
