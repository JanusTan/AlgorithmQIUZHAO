import random


#  归并排序
def twoSort(ls1, ls2):
    result = []
    len1, len2, i, j = len(ls1), len(ls2), 0, 0 # 双指针在两个子序列移动
    while i < len1 and j < len2: # 这两块在各自块内是有序的，因为mergeSort递归到最后是一个个单独元素
        if ls1[i] <= ls2[j]:
            result.append(ls1[i])
            i += 1
        else:
            result.append(ls2[j])
            j += 1
    result += ls1[i:] + ls2[j:]
    return result


def mergeSort(ls):
    # 递归终止条件： 各个子序列已分成单独的只有一个元素的序列
    if len(ls) == 1:
        return ls
    # 双斜杠除法向下取整，向下递归
    new_len = len(ls) // 2
    return twoSort(mergeSort(ls[: new_len]), mergeSort(ls[new_len:]))


if __name__ == "__main__":
    ls = []
    for i in range(10):
        ls.append(random.randint(1, 10))

    result = mergeSort(ls)
    print(ls)
    for r in result:
        print(r)