class Solution:
    def sortColors(self, nums: List[int]) -> None:
        maxi = max(nums)
        count = [0] * (maxi + 1)
        target = 0
        
        for num in nums:
            count[num] += 1
            
        for index, value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1
