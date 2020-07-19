# 283. 移动零
def moveZeroes(nums):
    i, j = 0, 0
    while j < len(nums):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i = i + 1
        j = j + 1
    return nums


a = [0,1,0,3,12]
print(moveZeroes(a)) # [1,3,12,0,0]