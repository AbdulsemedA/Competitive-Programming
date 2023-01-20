class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        answer = []
        
        for item in nums:
            answer.append(arr.index(item))
        
        return answer
        