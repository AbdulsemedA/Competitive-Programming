class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits = set()
        m, n = len(maze), len(maze[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in [0, m - 1]:
            for j in range(n):
                if maze[i][j] == ".":
                    exits.add((i, j))

        for i in [0, n - 1]:
            for j in range(m):
                if maze[j][i] == ".":
                    exits.add((j, i))
        
        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n
    
        def bfs(queue, dist):
            while queue:
                size = len(queue)
                dist += 1

                for _ in range(size):
                    x, y = queue.popleft()

                    for dx, dy in moves:
                        nx, ny = x + dx, y + dy

                        if inbound(nx, ny) and maze[nx][ny] == ".": 
                            if (nx, ny) in exits:
                                return dist

                            maze[nx][ny] = "#"
                            queue.append((nx, ny))
            return -1
        x, y = entrance
        maze[x][y] = "#"
        return bfs(deque([tuple(entrance)]), 0)