class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
            
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                
                elif j == n - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]

        return min(dp[-1])