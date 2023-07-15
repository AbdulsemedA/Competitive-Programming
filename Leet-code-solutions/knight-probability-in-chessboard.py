class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        board = [[0 for _ in range(n)] for _ in range(n)]
        board[row][column] = 1
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (-1, -2), (1, -2)]

        def inboard(i, j):
            return 0 <= i < n and 0 <= j < n
        
        for _ in range(k):
            newboard = [[0 for _ in range(n)] for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    for di, dj in directions:
                        if inboard(i + di, j + dj):
                            newboard[i + di][j + dj] += board[i][j] / 8
            
            board = newboard

        return sum([sum(row) for row in board])