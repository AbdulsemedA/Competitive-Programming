class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rep = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rep[(i, j)] = (i, j)
        
        moves = {
            1: set([(0, 1), (0, -1)]),
            2: set([(1, 0), (-1, 0)]),
            3: set([(0, -1), (1, 0)]),
            4: set([(0, 1), (1, 0)]),
            5: set([(-1, 0), (0, -1)]),
            6: set([(-1, 0), (0, 1)])
        }

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def find(x, y):
            while (x, y) != rep[(x, y)]:
                x, y = rep[(x, y)]    
            return x, y

        def union(x, y):
            for u, v in moves[grid[x][y]]:
                a, b = x + u, y + v
                if inbound(a, b):
                    if (-u, -v) in moves[grid[a][b]]:
                        ux, uy = find(x, y)
                        vx, vy = find(a, b)
                        if (ux, uy) != (vx, vy):
                            rep[(ux, uy)] = (vx, vy)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                union(i, j)
        
        return find(0, 0) == find(len(grid) - 1, len(grid[0]) - 1)