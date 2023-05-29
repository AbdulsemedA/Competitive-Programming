class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        nums = [0] * (n + 1)
        nums[0], nums[1] = 0, 1
        maxi = 1

        for i in range(2, n + 1):
            prev = i // 2

            if not i % 2:
                nums[i] = nums[prev]
            else:
                nums[i] = nums[prev] + nums[prev + 1]
            
            maxi = max(maxi, nums[i])
        
        return maxi