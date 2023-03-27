class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] == -abs(nums[index]):
                result.append(index + 1)
            nums[index] = -abs(nums[index])

        return result