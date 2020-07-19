# 15. 三数之和
# 讲出三种解法及其时间复杂度即可得到special offer hire
# 该函数时间复杂度：排序O(nlogn), 遍历数组双指针O(n)*O(n)=O(n^2)
# 空间复杂度： 只开了一个数组存有限个解集，所以是O(n)


def threeSum(nums):
    len1 = len(nums)
    if len1 < 3:
        return []
    result = []
    # 排序
    nums = sorted(nums)
    # 遍历数组，双指针找解，去除重复的解集
    for i in range(len1):
        if nums[i] > 0:  # 最小的都大于0了
            return result
        if i >= 1 and nums[i] == nums[i - 1] and nums[i] != 0:  # 和前面的target相同，跳过这个target
            continue
        L = i + 1
        R = len1 - 1
        while L < R:
            if nums[L] + nums[i] + nums[R] == 0:
                result.append([nums[L], nums[i], nums[R]])
                while L < R and nums[L] == nums[L + 1]:
                    L = L + 1
                while L< R and nums[R] == nums[R - 1]:
                    R = R - 1
                L = L + 1
                R = R - 1
            elif nums[L] + nums[i] + nums[R] > 0:
                R = R - 1
            elif nums[L] + nums[i] + nums[R] < 0:
                L = L + 1
    return result


a  = [0,0,0]
a1= [-1, 0, 1, 2, -1, -4]
print(threeSum(a))