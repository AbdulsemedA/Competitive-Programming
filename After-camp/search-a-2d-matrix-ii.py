class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, down = n - 1, 0

        while left > -1 and down < m:
            if matrix[down][left] == target:
                return True
            elif matrix[down][left] < target:
                down += 1
            else:
                left -= 1

        