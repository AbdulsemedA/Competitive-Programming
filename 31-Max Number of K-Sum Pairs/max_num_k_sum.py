import math
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        l = 0
        h = len(nums)-1
        while l < h:
            added = nums[l] + nums[h]
            if added == k:
                ans += 1
                l += 1
                h -= 1
            elif added < k:
                l += 1
            else:
                h -= 1
        return ans
