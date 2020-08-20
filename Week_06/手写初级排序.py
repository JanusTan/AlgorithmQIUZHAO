# 稳定的排序：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。不稳定（选堆快希）
# 冒泡排序：依次遍历每个下标，在遍历中两两比较，通过不断交换推出本轮遍历的最大值。时间复杂度O(n^2)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 选择排序: 依次遍历每个下标，每次遍历，都找剩余未排序最小的的下标，然后将最小值提到这个下标，时间复杂度O(n^2)
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


a = [3, 6, 11, 2, 8, 98]
print(selection_sort(a))
