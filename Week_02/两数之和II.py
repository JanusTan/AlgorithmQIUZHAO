# 167. 两数之和 II - 输入有序数组
# 时间复杂度O（n）, 空间O（n）


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic1={}
        for i, num in enumerate(numbers):
            if target-num in dic1: # 查询关键字是否在字典里
                if i+1>dic1[target-num]:
                    return [dic1[target-num], i+1]
                else:
                    return [i+1, dic1[target-num]]
            dic1[num] = i+1