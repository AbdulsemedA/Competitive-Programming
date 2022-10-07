from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        values = defaultdict(lambda : 0)
        result = 0
        current = 0
        for i in range(len(nums)): 
            current += nums[i]
            if current == k: 
                result += 1        
            if (current - k) in values:
                result += values[current - k]
            values[current] += 1
        return result
