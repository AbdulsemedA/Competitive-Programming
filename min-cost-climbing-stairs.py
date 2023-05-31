class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)

        def rec(x, n):
            if x >= n: return 0
            if x == n - 1: return cost[n-1]
            if x in memo: return memo[x]

            memo[x] = min(rec(x+2, n) + cost[x], cost[x] + rec(x+1, n))
            return memo[x]
        
        return min(rec(0, len(cost)), rec(1, len(cost)))