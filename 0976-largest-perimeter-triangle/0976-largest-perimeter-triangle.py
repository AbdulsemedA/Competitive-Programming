class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        
        for i in range(size - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                total = nums[i] + nums[i+1] + nums[i+2]
                return total
            
        return 0

        
