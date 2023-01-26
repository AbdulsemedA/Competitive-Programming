class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = last = 0
        counter = 1
        while last < len(nums):
            if nums[last] != nums[first]:
                counter += 1
                nums[first+1] = nums[last]
                first += 1
            last += 1
        return counter