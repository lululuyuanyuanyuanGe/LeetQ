class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_0, cols_0 = [], []
        rl = len(matrix)
        cl = len(matrix[0])

        for i in range(rl):
            for j in range(cl):
                if matrix[i][j] == 0:
                    rows_0.append(i)
                    cols_0.append(j)
        
        for i in range(rl):
            for j in range(cl):
                if i in rows_0 or j in cols_0:
                    matrix[i][j] = 0
        
        return matrix