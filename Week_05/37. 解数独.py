class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(itera = 0):
            # terminator
            if itera == len(unfilled): return True
            # current level logic
            # 获得一个要填的坐标
            row,colum = unfilled[itera]
            b = row//3*3+colum//3
            # 找能填的数字，并依次尝试填入这个坐标
            for temp_val in  rows[row] & colums[colum] & blocks[b]:
                rows[row].remove(temp_val)
                colums[colum].remove(temp_val)
                blocks[b].remove(temp_val)
                board[row][colum] = str(temp_val)
                # drill down
                if backtrack(itera+1):
                    return True
                # 回溯，找另外一个能填的
                rows[row].add(temp_val)
                colums[colum].add(temp_val)
                blocks[b].add(temp_val)
            return False

        # 确保各行各列各块里的不重复
        rows = [set(range(1,10)) for _ in range(9)] # set查询为O(1), [{1-9},{1-9},...]
        colums = [set(range(1,10)) for _ in range(9)]
        blocks = [set(range(1,10)) for _ in range(9)]
        # 在sets里去掉已填的数字，并记录没填的坐标
        # 坐标换算到对应的block = i//3*3 + j//3
        unfilled = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    rows[i].remove(val)
                    colums[j].remove(val)
                    blocks[i//3*3+j//3].remove(val)
                else:
                    unfilled.append([i,j])
        backtrack()
