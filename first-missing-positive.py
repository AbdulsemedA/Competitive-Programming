class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_map = {}
        mini = float("inf")
        maxi = float("-inf")
        for num in nums:
            if num >= 0:
                num_map[num] = 0
                mini = min(mini, num)
                maxi = max(maxi, num)
        
        if mini > 1:
            return 1
        if len(num_map) == maxi - mini + 1:
            return maxi + 1
        for i in range(mini, maxi):
            if i not in num_map:
                return i