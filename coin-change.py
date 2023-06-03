class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = defaultdict(int)
        n = len(coins)

        def dp(amount):
            if amount in memo: return memo[amount]
            if not amount: return 0
            mini = float('inf')

            for i in range(n):
                if coins[i] <= amount:
                    mini = min(mini, dp(amount - coins[i]))
                    
            memo[amount] = mini + 1
            return memo[amount]

        ans = dp(amount)
        return ans if ans != float('inf') else -1