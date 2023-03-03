class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        backup = -1

        if x == 0:
            return 0
        
        while left <= right:
            mid = left + (right - left) // 2
            backup = mid

            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                break
            
            if right < left:
                backup = right + (left - right) // 2

        return backup