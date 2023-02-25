from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        values = defaultdict(lambda : 0)
        result = curr = 0
        n = len(nums)
        
        for i in range(n): 
            curr += nums[i]
            
            if curr == k: 
                result += 1 
                
            if (curr - k) in values:
                result += values[curr - k]
                
            values[curr] += 1
            
        return result