class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
        
        def inBound(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])

        def dfs(i, j):
            count = 0
            
            for dx, dy in direction:
                if inBound(i + dx, j + dy):
                    if board[i + dx][j + dy] == "M":
                        count += 1

            if count: board[i][j] = str(count)
            else:
                board[i][j] = "B"

                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy

                    if inBound(nx, ny) and board[nx][ny] == "E":
                        board[nx][ny] == "B"
                        dfs(nx, ny)
            
        a, b = click
        if board[a][b] == "M":
            board[a][b] = "X"
        else:
            dfs(a, b)
        
        return board