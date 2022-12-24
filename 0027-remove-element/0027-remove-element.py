class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        frequency = nums.count(val)
        
        while frequency > 0:
            nums.remove(val)
            frequency -= 1
            
        size = len(nums)
        
        return size
        