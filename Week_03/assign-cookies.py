# 455. 分发饼干
# 时间复杂度O(n)，空间复杂度O(1)


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_fed = 0
        s_aten = 0
        while child_fed < len(g) and s_aten < len(s):
            if g[child_fed] <= s[s_aten]: # 贪心思想，每次都用最小的饼干喂最小的食量的孩子，那么最终会得到最优解，喂完就没退路
                child_fed += 1
            s_aten += 1
        return child_fed