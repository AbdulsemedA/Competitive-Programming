class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for num in nums:
                total += math.ceil(num / mid)
            if total > threshold:
                left = mid + 1
            else:
                right = mid - 1
                
        return left