class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_of_zeros = nums.count(0)
        
        for i in range(num_of_zeros):
            nums.remove(0)
            nums.append(0)
        