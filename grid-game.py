class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        grid[1] = [0] + grid[1]
        grid[0] += [0]
        n, mini = len(grid[0]), float("inf")

        for i in range(1, n):
            grid[1][i] += grid[1][i - 1]
            grid[0][n - 1 - i] += grid[0][n - i]
        for i in range(1, n):
            mini = min(mini, max(grid[0][i], grid[1][i - 1]))
        
        return mini