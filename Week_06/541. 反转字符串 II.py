class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 注意：string对象没有reverse成员函数，需要转换成list
        # 注意： reverse只能用于整个list翻转不能局部使用
        # list转换成string用到"".join(list1)
        if not s or k<=1: return s
        list1 = list(s)
        # 在0,2k,4k,6k...处开始i到i+k个字符reverse
        for i in range(0,len(list1),2*k):
            temp = list1[i:i+k]
            temp.reverse()
            list1[i:i+k] = temp
        return "".join(list1)