class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return []
        board = [['.'] * n for _ in range(n)]  # [['.', '.', '.'], ['.', '.', '.']]
        result = []

        def valid_coord(board, row, colum):  # 按行逐行递归，左右都是‘.’，因为设为‘Q’后会撤销回‘.’,整行只有当前这个Q
            # 正上方
            for i in range(row):
                if board[i][colum] == 'Q': return False
            # 左上方
            x, y = row, colum
            while x > 0 and y > 0:
                x, y = x - 1, y - 1
                if board[x][y] == 'Q': return False
            # 右上方
            x, y = row, colum
            while x > 0 and y < n - 1:
                x, y = x - 1, y + 1
                if board[x][y] == 'Q': return False
            return True

        def backtrack(board, row):
            # 递归终止条件
            if row == n:
                result.append(1)
                return
            # 回溯模板
            for colum in range(len(board[0])):
                # 判断当前点是否能加Q
                if not valid_coord(board, row, colum): continue
                # 选择加Q
                board[row][colum] = 'Q'
                # 递归下沉
                backtrack(board, row + 1)
                # 撤销加Q
                board[row][colum] = '.'

        backtrack(board, 0)
        return len(result)