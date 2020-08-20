class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 注意：空字符串和空字符串是同构的
        if not s: return True
        # 利用哈希表映射s的每个元素到t的每个元素
        # 当s[i]作为键值不在哈希表，触发False是t[i]是哈希表的值，否则映射起来。
        # 当s[i]作为键值在哈希表，触发False是t[i]不是键值s[i]哈希表的值
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values(): return False
                else: hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]: return False
        return True
