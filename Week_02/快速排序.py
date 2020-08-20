def quicksort(list1, left, right):
    # 递归终止条件
    if left >= right:
        return
    # 提取基准
    base = list1[left]
    start = left
    end = right

    # 当前层逻辑
    while left < right:
        while left < right and list1[left] < base:
            left = left + 1
        list1[right] = list1[left]
        while left < right and list1[right] >= base:
            right = right - 1
        list1[left] = list1[right]
    # 结束本次基准的循环后，即left = right
    list1[left] = base
    # 向下递归，基准左边的的子序列递归；基准右边的子序列递归
    quicksort(list1, start, left - 1)
    quicksort(list1, left + 1, end)


alist = [54, 26, 93, 17, 77, 31, 44, 54, 20]
quicksort(alist, 0, len(alist) - 1)
print(alist)