class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def dp(curr):
            if curr == 1:
                return 0
            
            if curr in memo:
                return memo[curr]
            
            if curr % 2:
                memo[curr] = 1 + dp(3 * curr + 1)
            else:
                memo[curr] = 1 + dp(curr // 2)
            
            return memo[curr]
        
        powers = []
        for ele in range(lo, hi+1):
            powers.append((dp(ele), ele))
        
        powers.sort()
        return powers[k-1][1]
        


        