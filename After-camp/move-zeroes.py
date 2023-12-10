class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeros_count = 0
        size = len(nums)
        
        for index in range(size):
            if nums[index] != 0:
                nums[non_zeros_count] = nums[index]
                non_zeros_count += 1
                
        zeros = non_zeros_count 
                
        while  zeros < size:
            nums[zeros] = 0
            zeros += 1
        