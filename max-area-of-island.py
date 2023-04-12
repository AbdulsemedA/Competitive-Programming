class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        dir_vector = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def inBound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
            
        def dfs(i, j):
            visited.add((i, j))
            area = 1

            for dx, dy in dir_vector:
                X = i + dx
                Y = j + dy

                if inBound(X, Y) and grid[X][Y] and (X, Y) not in visited:
                    area += dfs(X, Y)
        
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area