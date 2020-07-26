# 264. 丑数 II
# 时间复杂度O(nlogn), 动态规划时间复杂度是O(n)待做


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heappush, heappop
        queque = []
        visted = [1]
        factors = [2, 3, 5]
        heappush(queque,1)
        for _ in range(n):
            curr_ugly = heappop(queque)
            for factor in factors:
                new_ugly = factor * curr_ugly
                if new_ugly not in visted:
                    visted.append(new_ugly)
                    heappush(queque,new_ugly)
        return curr_ugly
