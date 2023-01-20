class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        return [index for index in range(n) if nums[index] == target]
        