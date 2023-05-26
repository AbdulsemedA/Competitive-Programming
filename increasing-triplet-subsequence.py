class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = sec_small = float('inf')
    
        for i in nums:
            if i <= small:
                small = i
            elif i <= sec_small:
                sec_small = i
            else:
                return True
    
        return False