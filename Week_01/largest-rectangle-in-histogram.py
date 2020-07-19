# 84. 柱状图中最大的矩形
# 两个独立的循环，时间复杂度O（n）, 维护一个栈空间O（n）


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 栈底是-1
        stack = [-1]
        result = 0
        # 制造单调递增的栈
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:
                temp = stack.pop()
                result = max(result, (i - stack[-1] - 1) * heights[temp])
            stack.append(i)
        # 清空栈
        for i in range(len(stack) - 1):
            temp = stack.pop()
            result = max(result, (len(heights) - 1 - stack[-1]) * heights[temp])
        return result

# 需要注意的测试样例：[1], [1,1]
