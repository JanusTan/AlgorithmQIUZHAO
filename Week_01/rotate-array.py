# 189. 旋转数组
# 时间复杂度：数组前插0（1），后弹出O（1），也就是循环体是O（1）,循环次数k次，所以是O（k*1）即O（n）
# 没开一位数组，所以空间复杂度O(1)


def rotate(nums, k):
    len1 = len(nums)
    k = k % len1 # 减少重复移动次数，如3个数移动五次和两次结果一样的
    for _ in range(k):
        nums.insert(0, nums.pop()) # 后弹出，在前插
    return nums


k, nums = 2, [-1,-100,3,99]
k1, nums1 = 3,[1,2,3,4,5,6,7]
print(rotate(nums1, k1))
