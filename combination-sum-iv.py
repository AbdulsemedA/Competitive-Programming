class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        size = len(nums)
        n = target

        def dp(idx, n):
            if n == 0: return 1
            state = (idx, n)

            if state in memo: return memo[state]

            for i in range(size):
                if nums[i] > n: continue
                memo[state] += dp(i, n - nums[i])
    
            return memo[state]

        return dp(0, n)