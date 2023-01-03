class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = [nums[nums[item]] for item in range(size)]
        
        return answer
        