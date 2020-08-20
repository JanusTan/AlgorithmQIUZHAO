class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先对每个区间按第一位从小到大排序，存入第一个区间，然后依次遍历剩下的区间，若能和弹出的栈顶区间合并，则替换掉掉栈顶
        # 否则存入这个区间。由于是排过序，所以只要判断前区间的第二位和新区间的第一位就可以决定是否合并
        if not intervals: return []
        def merge_two_inter(inter1, inter2):
            if inter1[1]>=inter2[0]: return [min(inter1[0],inter2[0]), max(inter1[1],inter2[1])]
        intervals = sorted(intervals, key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(1,len(intervals)):
           temp = merge_two_inter(result[-1], intervals[i])
           if temp: result[-1] = temp
           else: result.append(intervals[i])
        return result