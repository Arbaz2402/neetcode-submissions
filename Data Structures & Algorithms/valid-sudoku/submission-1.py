from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                # Ignore empty cells
                if num == ".":
                    continue

                # Find which 3x3 box this cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # Check duplicate
                if (
                    num in rows[r]
                    or num in cols[c]
                    or num in boxes[box_index]
                ):
                    return False

                # Add number
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True