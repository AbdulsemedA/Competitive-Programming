class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        sum_of_array = sum(nums)
        sum_ofIndex = sum(range(size + 1))
        missing = sum_ofIndex - sum_of_array
        
        return missing
        
        