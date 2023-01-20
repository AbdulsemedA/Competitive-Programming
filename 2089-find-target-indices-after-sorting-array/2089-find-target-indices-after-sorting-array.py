class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
    
        return [index for index in range(n) if sorted(nums)[index] == target]
        