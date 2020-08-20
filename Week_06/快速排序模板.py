# 先取头元素作为基准，然后使得基准左边的数小于它右边的数大于他，在对左右的子序列分别调用快速排序
def quicksort(begin, end, nums):
    # 递归终止条件
    if begin >= end: return
    # 当前层逻辑
    # 找出一个pivot使得其左边都是小于它的，右边都是大于等于它的
    pivot_position = find_pivot(begin, end, nums)
    # 分治
    quicksort(begin, pivot_position - 1, nums)
    quicksort(pivot_position + 1, end, nums)

def find_pivot(begin, end, nums):
    # 使基准左边的数小于它右边的数大于它：用一个下标标志pivot最终移动到的位置。
    # 遍历头元素之外的的所有元素，遇到小于基准的，标志右移一位并交换数字。
    # 所有数字遍历完后，交换头元素和标志所指的位置
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark


a = [3,6,11,2,8,98]
quicksort(0,len(a)-1,a)
print(a)