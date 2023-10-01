class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            diff = dp[i + 1][n - 1] - dungeon[i][n - 1]
            dp[i][n - 1] = max(1, diff)
        
        for j in range(n - 2, -1, -1):
            diff = dp[m - 1][j + 1] - dungeon[m - 1][j]
            dp[m - 1][j] = max(1, diff)

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = max(1, dp[i + 1][j] - dungeon[i][j])
                right = max(1, dp[i][j + 1] - dungeon[i][j])

                dp[i][j] = min(down, right)
                
        return dp[0][0]