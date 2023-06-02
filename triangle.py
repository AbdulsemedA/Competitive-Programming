class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = defaultdict(int)
        n = len(triangle)

        def dp(lvl, idx):
            state = (lvl, idx)

            if lvl == n or idx == len(triangle[lvl]): return 0
            if lvl == n - 1:
                if idx < len(triangle[lvl]):
                    return triangle[lvl][idx]
            
            if state in memo: return memo[state]

            Min = min(dp(lvl + 1, idx), dp(lvl + 1, idx + 1))
            memo[state] = triangle[lvl][idx] + Min

            return memo[state]
        
        return dp(0, 0)