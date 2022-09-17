class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=lambda x: (len (x), x))
        nums = nums[:len(nums)-k+1]
        return nums[len(nums)-1]
