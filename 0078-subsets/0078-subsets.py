class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for i in range(2 ** len(nums)):
            subsets.append([])
            idx = 0
            while i > 0:
                if i & 1:
                    subsets[-1].append(nums[idx])
                idx += 1
                i >>= 1
        
        return subsets
                    
                    
