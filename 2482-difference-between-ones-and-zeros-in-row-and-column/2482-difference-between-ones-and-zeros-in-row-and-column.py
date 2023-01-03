class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        zeros_col = []
        ones_col = []
        zeros_row = []
        ones_row  = []
        
        diff = [[0 for _ in range(m)] for _ in range(n)]
        
        for item in grid:
            total = sum(item)
            ones_row.append(total)
            zeros_row.append(m - total)
        
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
        
        