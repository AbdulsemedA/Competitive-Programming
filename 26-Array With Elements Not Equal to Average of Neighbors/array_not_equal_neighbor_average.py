import math

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [None] * len(nums)
        if (len(nums)%2) == 0:
            middle = int(len(nums)/2) + 1
        else:
            middle = math.ceil(len(nums)/2)
        m = 1
        for i in range(middle-1):
            if m < len(nums):
                result[m] = nums[i]
                m+=2
        k = 0
        for i in range(middle-1,len(nums)):
            if k < len(nums):
                result[k] = nums[i]
                k+=2
        return result
