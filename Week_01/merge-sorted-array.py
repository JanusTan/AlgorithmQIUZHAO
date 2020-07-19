# 88. 合并两个有序数组,时间复杂度O（m+n）,空间复杂度O（n）


def merge(nums1,nums2,m,n):
    i = 0
    j = 0
    copy_nums = nums1[:m]
    nums1[:] = []
    while i < m and j < n:
        if copy_nums[i] <= nums2[j]:
            nums1.append(copy_nums[i])
            i += 1
        elif copy_nums[i] > nums2[j]:
            nums1.append(nums2[j])
            j += 1
    if i < m:
        nums1[i + j:] = copy_nums[i:]
    elif j < n:
        nums1[i + j:] = nums2[j:]
    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m,n=3,3
print(merge(nums1,nums2,m,n))