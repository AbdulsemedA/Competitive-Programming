class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = float("-inf")
        prefix = []
        curr = 0
        
        for i in range(n):
            prefix.append(nums[i] + curr)
            curr += nums[i]
        
        curr = prev = 0
            
        for i in range(k - 1, n):
            average = prefix[i] - prev
            max_avg = max(max_avg, average/ k)
            prev = prefix[curr]
            curr += 1
        
        return max_avg
        
        