# 347. 前 K 个高频元素
# 第一个排序字典的方法时间复杂度是O(nlogn)， 第二个使用堆的是O(nlogk)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # dic = Counter(nums)
        # dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
        # return list(map(lambda x:x[0], dic))[:k]

        # heapq
        from heapq import heappush, heappop
        queque, res = [], []
        from collections import Counter
        dic = Counter(nums)
        for i in dic:
            heappush(queque, (-dic[i],i))
        for j in range(k):
            temp = heappop(queque)
            res.append(temp[1])
        return res