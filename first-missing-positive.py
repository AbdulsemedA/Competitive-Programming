class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_map = {}
        mini = float("inf")
        maxi = float("-inf")
        size = 0
        for num in nums:
            if num >= 0 and num not in num_map:
                num_map[num] = 0
                size += 1
                mini = min(mini, num)
                maxi = max(maxi, num)
        
        if mini > 1:
            return 1
        if size == maxi - mini + 1:
            return maxi + 1
        for i in range(mini, maxi):
            if i not in num_map:
                return i