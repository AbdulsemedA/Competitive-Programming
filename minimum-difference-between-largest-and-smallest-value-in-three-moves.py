class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        nums.sort()
        k, mini = len(nums) - 1, float("inf")
        for i in range(4): mini = min(mini, nums[k + i - 3] - nums[i])
        return mini