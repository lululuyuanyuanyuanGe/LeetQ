class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotate_matrix = []
        for c in range(len(matrix[0])):
            rotate_row = []
            for r in range(len(matrix)):
                rotate_row.append(matrix[r][c])
            rotate_row.reverse()
            rotate_matrix.append(rotate_row)
        matrix[:] = rotate_matrix