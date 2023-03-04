class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total = curr = 0
        prefix = {0:1}

        for i in nums:
            curr += i
            total += prefix.get(curr - goal, 0)
            prefix[curr] = 1 + prefix.get(curr, 0)
        
        return total