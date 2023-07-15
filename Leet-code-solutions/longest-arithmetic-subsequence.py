class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        
        for ele in range(1, n):
            for i in range(ele):
                diff = nums[ele] - nums[i]
                
                if (i, diff) in dp:
                    dp[(ele, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(ele, diff)] = 2
        
        return max(dp.values())