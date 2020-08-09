# 621. 任务调度器
# 时间复杂度O(nlogn), 空间复杂度O(n)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 最优解，思路是DP
        # DP状态定义：dp[i][j]不好找，也就是DP走不通。贪心呢？
        # 根据题目推理，由最高频的任务的次数count0决定最短任务时间。(count0 - 1)*(n+1) + count1, count1为同样高频的的任务个数包括count0那种情况
        # 当式子的结果比所有任务的个数还小，就返回任务个数
        length = len(tasks)
        if length <= 1:
            return length
        from collections import Counter
        dic = Counter(tasks)
        list1 = sorted(list(dic.values()), reverse = True)
        count0 = list1[0]
        result = (count0 - 1)*(n+1)
        for i in list1:
            if i==count0:
                result += 1
        return result if result>length else length