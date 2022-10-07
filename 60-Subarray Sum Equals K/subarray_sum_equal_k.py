from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
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
