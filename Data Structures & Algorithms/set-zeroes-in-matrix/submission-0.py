class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        # Check if first column contains zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True

        # Use first row and column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Set inner matrix elements to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Handle first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Handle first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0