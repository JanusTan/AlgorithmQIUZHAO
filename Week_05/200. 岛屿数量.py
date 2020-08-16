class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows = len(grid)
        columns = len(grid[0])
        result = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    result +=1
                    grid[i][j] = '0' # 复制=和判断==，容易敲多一个等号然后debug不出
                    # 对这个格子开始BFS
                    queue = [[i,j]]
                    while queue:
                        x,y=queue.pop(0) # i,j上面已经用了，这里不能用i,j
                        for new_x, new_y in [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]:
                            if 0 <= new_x < rows and 0 <= new_y < columns and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                queue.append([new_x,new_y])
        return result