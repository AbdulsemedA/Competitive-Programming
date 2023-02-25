class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        n = len(nums)
        
        for i in range(1,n):
            curr = nums[i-1]
            nums[i] += curr
            
        return nums