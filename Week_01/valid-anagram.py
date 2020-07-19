# 242. 有效的字母异位词
# 时间复杂度O（n）, 空间O（n）


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 更简单的return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        dic = {}
        for key in s:
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        for key in t:
            if key in dic:
                dic[key] -= 1
            else:
                return False
        for value in dic.values():
            if value == 0:
                continue
            else:
                return False
        return True