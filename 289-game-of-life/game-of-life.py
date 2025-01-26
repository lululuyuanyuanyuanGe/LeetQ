class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row, col = len(board), len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(row):
            for j in range(col):
                livecount = 0
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    if 0 <= nr < row and 0 <= nc < col and abs(board[nr][nc]) == 1:
                        livecount += 1
                if board[i][j] == 1:
                    if livecount < 2 or livecount > 3:
                        board[i][j] = -1
                    
                else:
                    if livecount == 3:
                        board[i][j] = 2
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                            

