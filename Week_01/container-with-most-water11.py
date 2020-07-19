# 11. 盛最多水的容器
def maxArea(height):
    left = 0
    right = len(height) - 1
    if right == 0:
        return 0
    max_area = min(height[left], height[right]) * (right - left) # 取最短度的板乘以宽度
    while left < right:
        if height[left] < height[right]:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            left = left + 1
        elif height[right] <= height[left]:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            right = right - 1
    return max_area


a = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(a))
