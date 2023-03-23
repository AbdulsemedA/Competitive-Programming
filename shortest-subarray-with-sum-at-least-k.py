class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float('inf')
        nums.append(0)
        s = deque([-1])

        for i in range(n):
            nums[i] += nums[i-1]
            while s and ans + s[0] <= i:
                s.popleft()
            while s and nums[s[0]] + k <= nums[i]: 
                ans = i - s.popleft()
            while s and nums[s[-1]] >= nums[i]: 
                s.pop()
            s.append(i)

        return ans if ans != float('inf') else -1