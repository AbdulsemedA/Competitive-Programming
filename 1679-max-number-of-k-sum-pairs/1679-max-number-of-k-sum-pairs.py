import math
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans, left, right = 0, 0, n - 1
        
        while left < right:
            sums = nums[left] + nums[right]
            if sums == k:
                ans += 1
                left += 1
                right -= 1
            elif sums < k:
                left += 1
            else:
                right -= 1
                
        return ans