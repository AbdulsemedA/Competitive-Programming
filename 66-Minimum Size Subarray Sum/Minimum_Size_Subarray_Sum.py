class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        else:
            mini = len(nums) 
            first = last = 0
            current_sum = 0
            while last < len(nums):
                current_sum += nums[last]
                while current_sum >= target:
                    mini = min(mini, last - first + 1)
                    current_sum -= nums[first]
                    first += 1
                last += 1
        return mini
