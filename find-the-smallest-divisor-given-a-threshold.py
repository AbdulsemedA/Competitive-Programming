class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        divisors = [x for x in range(1, nums[-1] + 1)]
        left, right = 0, len(divisors) - 1

        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for num in nums:
                total += math.ceil(num / divisors[mid])
            if total > threshold:
                left = mid + 1
            else:
                right = mid - 1
                
        return divisors[left]