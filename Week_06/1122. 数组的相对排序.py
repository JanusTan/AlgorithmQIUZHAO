class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 因为能取到的数字最高位1000，最低为0，所以工1001个数
        count = [0]*1001
        result = []
        # 统计要排序的数出现次数
        for i in arr1:
            count[i] += 1
        # 按arr2顺序输出
        for j in arr2:
            result += [j] * count[j]
            count[j] = 0
        # 将未在arr2的元素按升序输出
        for k in range(1001):
            result += [k] * count[k]
        return result
