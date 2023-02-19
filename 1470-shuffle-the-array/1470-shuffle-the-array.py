class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        n = len(nums)
        i, j = 0, (n // 2)
             
        while j < n:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        
        return res
            
        