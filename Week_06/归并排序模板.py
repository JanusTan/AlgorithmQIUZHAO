# 先将数组一分为二，分别递归此函数，直到数组长度为1。合并这两个一分为二的数组
def split_merge(list_all):
    # 递归终止条件
    if len(list_all) == 1: return list_all
    # 分治split and merge
    split_idx = len(list_all) // 2
    return two_sort(split_merge(list_all[:split_idx]), split_merge(list_all[split_idx:]))

def two_sort(ls1, ls2):
    # 归并两有序的子序列，双指针
    len1, len2 = len(ls1), len(ls2)
    i, j = 0, 0
    result = []
    while i < len1 and j < len2:
        if ls1[i] <= ls2[j]:
            result.append(ls1[i])
            i += 1
        else:
            result.append(ls2[j])
            j += 1
    result += ls1[i:] + ls2[j:] # 不能用append，会变成二维的
    return result


a = [2, 1, 3, 4, 2, 5, 3, 9]
print(split_merge(a))
