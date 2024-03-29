class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a % b)

        a, b = max(nums), min(nums)      
        return GCD(a, b)