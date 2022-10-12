class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums2 = []
        for i in range(len(nums)):
            if k > 0:
                if i >= len(nums) - k:
                    nums2.append(nums[i])
        for j in range(len(nums) - k):
            nums2.append(nums[j])
        nums.clear()
        for m in nums2:
            nums.append(m)
