class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {i: [i, 0] for i in range(row * col + 2)}
        top, bottom = row * col, row * col + 1
        grid = [[0] * col for _ in range(row)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbounds(i, j):
            return 0 <= i < row and 0 <= j < col
        
        def finder(x):
            while x != rep[x][0]:
                x = rep[x][0]
            return x
        
        def union(x, y):
            fst = finder(x)
            snd = finder(y)

            if fst != snd:
                if rep[fst][1] <= rep[snd][1]:
                    rep[fst][0] = snd
                    rep[snd][1] += 1 + rep[fst][1]
                else:
                    rep[snd][0] = fst
                    rep[fst][1] += 1 + rep[snd][1]
        
        def pos(x, y): return x * col + y

        for idx in range(len(cells) - 1, -1, -1):
            x, y = cells[idx]
            x, y = x - 1, y - 1
            grid[x][y] = 1

            if x == 0: union(pos(x, y), top)
            if x == row - 1: union(pos(x, y), bottom)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if inbounds(nx, ny):
                    if grid[nx][ny]:
                        union(pos(x, y), pos(nx, ny))
            
            if finder(top) == finder(bottom): return idx

        return -1