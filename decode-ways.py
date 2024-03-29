class Solution:
    def numDecodings(self, s: str) -> int:
        memo = defaultdict(int)
        n = len(s)
        
        def dp(idx):
            if idx == n: return 1
            if idx in memo: return memo[idx]
            if s[idx] == '0': return 0

            count = dp(idx + 1)
            if idx < n - 1:
                if int(s[idx]) and int(s[idx: idx + 2])in range(1, 27):
                    count += dp(idx + 2)

            memo[idx] = count
            return count
        
        return dp(0)