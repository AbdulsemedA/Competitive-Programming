class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_of_zeros = nums.count(0)
        for i in range(num_of_zeros):
            nums.remove(0)
            nums.append(0)
