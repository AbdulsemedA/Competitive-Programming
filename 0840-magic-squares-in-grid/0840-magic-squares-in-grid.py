class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        counter = 0
        
        for local in range(len(grid) - 2):
            for loc in range(len(grid[0]) - 2):
                unique = set()
                d1 = d2 = 0
                row_sum = [0] * 3
                col_sum = [0] * 3
                
                for row in range(local, local + 3):
                    d1 += grid[row][row - local + loc]
                    d2 += grid[row][loc + 2 + local - row]
                    
                    for col in range(loc, loc + 3):
                        row_sum[row % 3] += grid[row][col]
                        col_sum[col % 3] += grid[row][col]
                        
                        if grid[row][col] > 0 and grid[row][col] < 10:
                            unique.add(grid[row][col])
                    
                if len(unique) == 9:
                    if row_sum.count(row_sum[0]) == col_sum.count(col_sum[0]) == 3:
                        if row_sum[0] == d1 == d2:
                            counter += 1
        
        return counter