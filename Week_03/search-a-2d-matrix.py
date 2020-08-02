# 74. 搜索二维矩阵
# 时间复杂度O(log(m*n))， 空间复杂度O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = m*n-1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid//n][mid%n] > target:  # 升序，在左边的序列
                right = mid - 1
            elif matrix[mid//n][mid%n] < target: # 升序，在右边的序列
                left = mid + 1
            else:  # 找到了
                return True
        return False

