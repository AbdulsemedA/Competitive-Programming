class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        current = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if current == (total_sum - nums[i] - current):
                return i
            current += nums[i]
        return -1
