class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        maximum = 0
        size = len(nums)
        if nums.count(0) <= 1:
            return size - 1
        for i in range(size-1):
            if nums[i] != 0:
                left += 1
            else:
                for j in range(i+1,size):
                    if nums[j] != 0:
                        right += 1
                    else:
                        break
                maximum = max(left + right, maximum)
                left = right = 0 
        return maximum

            

            
        
