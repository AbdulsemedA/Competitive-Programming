class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for num in piles:
                total += math.ceil(num / mid)
            if total > h:
                left = mid + 1
            else:
                right = mid - 1
                
        return left