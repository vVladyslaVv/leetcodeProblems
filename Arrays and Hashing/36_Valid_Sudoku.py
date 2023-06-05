from collections import defaultdict
from typing import List


# So we create default dictionaries for columns, rows and boxes. Then we iterate threw our matrix and if the value
# isn't empty (.) we check if value is already in either rows, columns or boxes. After that we write down current
# value to rows, columns and boxes dictionaries. The main idea behind boxes, is that we use integer division to
# differentiate in which of the 3x3 boxes we are right now and add value to the correspondent box
# (we use coordinates of 3x3 box as tuple for key in that dictionary)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[
                    (row // 3, col // 3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3, col // 3)].add(board[row][col])
        return True
