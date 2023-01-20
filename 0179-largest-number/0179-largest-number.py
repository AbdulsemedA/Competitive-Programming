class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        if sum(nums) == 0:
            return "0"
        
        for item in range(size):
            nums[item] = str(nums[item])
        
        for i in range(size):
            for j in range(size - i - 1):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        return ''.join(nums)
        