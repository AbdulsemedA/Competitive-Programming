class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ranges = int(sqrt(c))
        left, right = 0, ranges
        
        while left <= right:
            if left ** 2 + right ** 2 > c:
                right -= 1
            elif left ** 2 + right ** 2 < c:
                left += 1
            else:
                return True
        
        return False
            
        