class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        direction = [(1,0), (0, 1)]

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if (i, j) == (m - 1, n - 1): return 1
            
            for x, y in direction:
                a, b = i + x, j + y
                
                if inbound(a, b):
                    memo[(i, j)] += dp(a, b)
            
            return memo[(i, j)]
        
        return dp(0, 0)