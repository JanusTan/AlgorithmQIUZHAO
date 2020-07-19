# 239. 滑动窗口最大值
# 遍历一遍nums数组，时间复杂度O（n），空间复杂度O(n)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result =[]
        from collections import deque
        deque1 = deque()
        for i, num in enumerate(nums):
            while deque1 and deque1[0] <= i-k: # i=k的时候开始删除过期的队首
                deque1.popleft()
            while deque1 and num > nums[deque1[-1]]: # 队尾小于当前的值就要删掉
                deque1.pop()
            deque1.append(i)
            if i >=k-1: # 遍历到k个时和之后，都要存每一步最大的值
                result.append(nums[deque1[0]])
        return result