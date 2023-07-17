class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        positive = [0] * len(nums)
        negative = [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                positive[i] = negative[i-1] + 1
                negative[i] = negative[i-1]
                
            elif nums[i] < nums[i-1]:
                positive[i] = positive[i-1]
                negative[i] = positive[i-1] + 1
            else:
                positive[i] = positive[i-1]
                negative[i] = negative[i-1]
        
        return max(positive[-1], negative[-1]) + 1