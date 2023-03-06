class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            day = curr = 0
            l = r = 0

            while r < len(weights):
                curr += weights[r]

                if curr > mid:
                    day += 1
                    l = r
                    curr = weights[l]
                
                r += 1
            if weights[r-1] <= mid:
                day += 1
            
            if day > days:
                left = mid + 1
            elif day <= days:
                if mid >= max(weights):
                    right = mid - 1
                else:
                    left = mid + 1
            
        return left