# 529. 扫雷游戏
# # 时间复杂度O(nlogn)，递归树的深度，空间复杂度O(1)


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, r, c):
            # terminator
            if board[r][c] != 'E':
                return

            # current level
            # mines numbers(8 direction search)
            count = 0
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < max_r and 0 <= new_c < max_c and board[new_r][new_c] == 'M':
                    count += 1

            if count == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(count)
                return # 终止当前递归

            # drill down next 8 neighbor
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < max_r and 0 <= new_c < max_c:
                    dfs(board, new_r, new_c)

        if not board:
            return []
        r0, c0 = click[0], click[1]
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        max_r = len(board)
        max_c = len(board[0])
        if board[r0][c0] == 'M':
            board[r0][c0] = 'X'
            return board
        dfs(board, r0, c0)
        return board