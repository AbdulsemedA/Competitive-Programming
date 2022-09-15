class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for item in range(len(nums)):
            if nums[item] == target:
                result.append(item)
        return result
