class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n, count = len(nums), 0

        for i in range(n):
            ans = nums[i]
            for j in range(i,n):
                ans = math.gcd(ans,nums[j])
                if ans == k:
                    count += 1
                elif ans < k:
                    break

        return count