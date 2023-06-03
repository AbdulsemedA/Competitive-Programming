class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        def rec(x, n):
            if x >= n: return 0
            if x == n - 1: return nums[n-1]
            if x in memo: return memo[x]

            memo[x] = max(nums[x] + rec(x+2, n), rec(x+1, n))
            return memo[x]
        
        return rec(0, len(nums))