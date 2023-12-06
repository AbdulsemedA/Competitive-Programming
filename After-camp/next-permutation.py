class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n > 1:
            r = n - 1
            prev = nextn = -1
            
            while r:
                if nums[r] > nums[r-1]:
                    prev = r-1
                    break
                r -= 1
                
            if prev == -1:
                for i in range(n//2):
                    nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            
            else:
                nx = n - 1
                
                while nx > 0:
                    if nums[nx] > nums[prev]:
                        nextn = nx
                        break
                    nx -= 1
                
                nums[prev], nums[nextn] = nums[nextn], nums[prev]
                temp = sorted(nums[prev + 1:])
                
                for i in range(len(temp)):
                    nums[prev + 1 + i] = temp[i]

        
        