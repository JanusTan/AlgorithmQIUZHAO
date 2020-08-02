# 874. 模拟行走机器人
# 时间复杂度O(n)， 空间复杂度O(1)有限的元素


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction_id = 0
        # move = [[0,1], [-1,0],[0,-1],[1,0]] # 超时
        move, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0), ], set(map(tuple, obstacles)) # obstacles要存为tuple元组类型的set
        # 才不超时，set查询比list快是O(1)，list是O(n)！
        x=y=0
        max_dis = 0
        for command in commands:
            if command == -2: direction_id = (direction_id + 1) % 4
            elif command == -1: direction_id = (direction_id - 1) % 4
            else:
                dx, dy = move[direction_id]
                while command and (x+dx, y+dy) not in obstacles:
                    x += dx
                    y += dy
                    command -=1
            max_dis = max(max_dis, x ** 2 + y ** 2) # 贪心的思想，每次command的最优则为全局的的最优，不能回头
        return max_dis

