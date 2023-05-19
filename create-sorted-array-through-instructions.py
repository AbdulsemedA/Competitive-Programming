class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0
        
        for i in instructions:
            if not nums: nums.append(i)
            else:
                less = bisect.bisect_right(nums, i)
                great = bisect.bisect_left(nums, i)
                cost  += min(great, len(nums) - less)
                nums.insert(less, i)
                
        return cost % (10**9 +7)