class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        index = 0
        non_zeros_count = 0
        size = len(nums)
        
        while index < size - 1:
            if nums[index] == nums[index+1]:
                nums[index] *= 2
                nums[index+1] = 0
                index += 1
            index += 1
        
        for index in range(size):
            if nums[index] != 0:
                nums[non_zeros_count] = nums[index]
                non_zeros_count += 1
                
        while non_zeros_count < size:
            nums[non_zeros_count] = 0
            non_zeros_count += 1
        
        return nums
                
        