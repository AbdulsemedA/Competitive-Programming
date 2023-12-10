class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        counter = 0

        def bound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        
        def dfs(i, j):
            nonlocal counter
            visited.add((i, j))

            for dx, dy in direction:
                X = i + dx
                Y = j + dy

                if bound(X, Y) and grid[X][Y]:
                    if grid[X][Y] and (X, Y) not in visited:
                        dfs(X, Y)
                else: 
                    counter += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    dfs(i, j)
        
        return counter




            


        