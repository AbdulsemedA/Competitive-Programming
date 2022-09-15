class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j+1]:
                    x = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = x 
