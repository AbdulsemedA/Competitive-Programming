class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1 = defaultdict(int)
        memo2 = defaultdict(int)

        def rec(x, n, memo):
            if x >= n: return 0
            if x == n - 1: return nums[n-1]
            if x in memo: return memo[x]

            memo[x] = max(nums[x] + rec(x+2, n, memo), rec(x+1, n, memo))
            return memo[x]
        
        if len(nums) == 1: return nums[0]
        return max(rec(0, len(nums) - 1, memo1), rec(1, len(nums), memo2))