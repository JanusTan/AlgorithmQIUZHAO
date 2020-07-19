# 49. 字母异位词分组
# 时间复杂度O（n）, 空间O（1）


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for item in strs:
            key = tuple(sorted(item)) # 排序后作为key，tuple是记为不可修改元组
            dict[key] = dict.get(key, []) + [item] # 字典的get函数是返回该key下所有values
        return list(dict.values())