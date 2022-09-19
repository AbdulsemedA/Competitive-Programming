class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        large = 0
        for i in range(int(len(nums)/2)):
            if nums[i] + nums[len(nums)-1-i] >= large:
                large = nums[i] + nums[len(nums)-1-i]
        return large
