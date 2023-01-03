class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        zeros_col = []
        ones_col = []
        
        diff = [[0 for _ in range(m)] for _ in range(n)]
        zeros_row = [(m - grid[i].count(1)) for i in range(n)]
        ones_row = [grid[i].count(1) for i in range(n)]
        
        for col in range(m):
            ones_col.append(0)
            zeros_col.append(0)
            for row in range(n):
                cell = grid[row][col]
                if cell == 1:
                    ones_col[-1] += 1
                else:
                    zeros_col[-1] += 1
        
        for sub in range(n):
            for val in range(m):
                diff[sub][val] = ones_row[sub] + ones_col[val] - zeros_row[sub] - zeros_col[val]
        
        return diff
        
        