class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        n = len(nums)

        def dp(idx, curr):
            if idx == n:
                if curr == target: return 1
                return 0
            
            state = (idx, curr)
            if state in memo: return memo[state]
            memo[state]= dp(idx + 1, curr + nums[idx]) + dp(idx + 1, curr - nums[idx])
            
            return memo[state]
        
        return dp(0, 0)