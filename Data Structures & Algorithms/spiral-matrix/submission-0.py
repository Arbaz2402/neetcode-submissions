class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # LEFT → RIGHT
            for c in range(left, right + 1):
                ans.append(matrix[top][c])

            top += 1

            # TOP → BOTTOM
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])

            right -= 1

            # RIGHT → LEFT
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])

                bottom -= 1

            # BOTTOM → TOP
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])

                left += 1

        return ans