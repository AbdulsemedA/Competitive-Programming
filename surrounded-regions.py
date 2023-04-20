class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        unflipped = set()
        visited = set()
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inBound(x, y):
            return 0 <= x < m and 0 <= y < n

        def dfs(i, j):
            if not inBound(i, j) or board[i][j] == "X" or (i, j) in visited:
                return
            visited.add((i, j))
            if board[i][j] == "O":
                unflipped.add((i, j))
                
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    dfs(nx, ny)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in unflipped:
                    board[i][j] = 'X'
                    
        return board