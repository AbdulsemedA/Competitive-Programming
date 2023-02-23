class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        mini = 0
        n = len(nums)
        
        if total >= target:
            mini = n
            
        left = right = 0
        curr_sum = 0
        
        while right < n:
            curr_sum += nums[right]
            
            if curr_sum >= target:
                while curr_sum >= target:
                    mini = min(mini, right - left + 1)
                    curr_sum -= nums[left]
                    left += 1
                
            
            right += 1
        
        return mini
            
        