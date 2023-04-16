class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        counter = 0

        def bound(x, y):
            return 0 <= x < len(grid2) and 0 <= y < len(grid2[0])
        
        def dfs(i, j):
            nonlocal valid
            visited.add((i, j))
            
            for dx, dy in direction:
                X = i + dx
                Y = j + dy

                if bound(X, Y) and grid2[X][Y] and (X,Y) not in visited:
                    if not grid1[X][Y]:
                        valid = False
                    dfs(X, Y)
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] and (i, j) not in visited:
                    valid = True
                    if not grid1[i][j]:
                        continue
                    dfs(i, j)
                    if valid: counter += 1
        
        return counter