class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum

        while left <= right:
            mid = (left + right) // 2
            curr = mid * (mid + 1) // 2
            l_side, r_side = curr, curr - mid
            size = 0
            
            if index < mid:
                l_side -= ((mid - index - 1) * (mid - index) // 2)
            
            if n - index - 1 < mid - 1:
                r_side -= ((mid - n + index) * (mid - n + index + 1) // 2)

            if index + 1 - mid > 0:
                size += index + 1 - mid
            
            if index + mid - 1 < n - 1:
                size += n - index - mid
            
            total = l_side + r_side + size
            
            if total > maxSum:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return right
