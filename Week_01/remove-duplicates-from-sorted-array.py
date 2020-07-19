# 26. 删除排序数组中的重复项
# 时间复杂度O（n）, 空间O（1）


def removeDuplicates(nums):
    idx = 0
    for i, num in enumerate(nums):
        if nums[i] != nums[idx]:
            idx += 1
            nums[idx] = nums[i]
    nums = nums[:idx+1]
    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1,1,2]
print(removeDuplicates(nums2))