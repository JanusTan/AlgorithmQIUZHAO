# 42. 接雨水
# 时间复杂度O（n）, 空间O（1）

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3: return 0
        res, idx = 0, 0
        stack = []
        while idx < length:
            while len(stack) > 0 and height[idx] > height[stack[-1]]:
                top = stack.pop()  # index of the last element in the stack
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[idx]) - height[top]
                dist = idx - stack[-1] - 1
                res += (dist * h)
            stack.append(idx)
            idx += 1
        return res