class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros_count = 0
        size = len(nums)
        
        for index in range(size):
            if nums[index] != 0:
                nums[non_zeros_count] = nums[index]
                non_zeros_count += 1
                
        while non_zeros_count < size:
            nums[non_zeros_count] = 0
            non_zeros_count += 1
        