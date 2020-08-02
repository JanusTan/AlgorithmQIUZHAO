# 200. 岛屿数量
# # 时间复杂度O(n^2)，空间复杂度O(n)，开了一个队列


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    count += 1
                    # BFS template
                    from collections import deque
                    queue = deque()
                    queue.append([i, j])
                    while queue:
                        x, y = queue.popleft()
                        for new_x, new_y in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                            if 0 <= new_x < row and 0 <= new_y < column and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                queue.append([new_x, new_y])
        return count
