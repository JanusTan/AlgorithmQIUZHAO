# 169. 多数元素
# 时间复杂度O(nlogn), 空间复杂度O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
        if dic[0][1] > len(nums)//2:
            return dic[0][0]
