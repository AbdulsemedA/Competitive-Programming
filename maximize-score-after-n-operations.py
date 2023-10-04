class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def TD(state, operation):
            maxi = 0
            
            for i in range(n):
                for j in range(i+1, n):
                    if (state >> (n - i - 1)) & 1 or (state >> n - j - 1) & 1:
                        continue
                    state |= (1 << n - i - 1)
                    state |= (1 << n - j - 1)
        
                    curr = TD(state, operation + 1) + operation * gcd(nums[i], nums[j])
                    maxi = max(maxi, curr)
                    
                    state = state ^ (1 << n - j - 1)
                    state = state ^ (1 << n - i - 1)
                    
            return maxi
                    
        
        return TD(0, 1)