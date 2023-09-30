class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def LCS(s1, s2):
            r, c = len(s1), len(s2)
            dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

            for i in range(r - 1, -1, -1):
                for j in range(c - 1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
            return dp[0][0]
        
        return LCS(s, s[::-1])