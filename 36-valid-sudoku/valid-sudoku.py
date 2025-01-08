class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in row_sets[r]:
                    return False
                row_sets[r].add(num)

                if num in col_sets[c]:
                    return False
                col_sets[c].add(num)

                box_index = (r // 3) * 3 + c // 3
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        return True