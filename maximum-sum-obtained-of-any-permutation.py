class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n, total = len(nums), 0
        nums.sort()
        prefix = [0] * (n+1)

        for first, last in requests:
            prefix[first] += 1
            prefix[last+1] -= 1

        for i in range(1,n):
            prefix[i] += prefix[i-1]

        prefix.pop()
        prefix.sort()

        for i in range(n):
            total += prefix[i] * nums[i]
            total %= ((10 ** 9) + 7)
        
        return total