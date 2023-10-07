class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1: continue
                down = max(1, dp[i + 1][j] - dungeon[i][j])
                right = max(1, dp[i][j + 1] - dungeon[i][j])

                dp[i][j] = min(down, right)
        
        return dp[0][0]