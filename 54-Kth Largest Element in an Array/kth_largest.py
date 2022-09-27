class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums = nums[:len(nums)-k+1]
        return max(nums)
