class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            maxi = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, dp[j] + 1)
            dp[i] = maxi
        
        return max(dp)
        