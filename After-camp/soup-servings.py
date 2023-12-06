class Solution:
    def soupServings(self, N: int) -> float:
        N = (N + 24) // 25
        memo = {}

        if N >= 200: return 1.0
        def dp(a: int, b: int) -> float:
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            memo[(a, b)] = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) +
                                    dp(a - 2, b - 2) + dp(a - 1, b - 3))
            return memo[(a, b)]

        return dp(N, N)