class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        first = last = current = counter = maxi = 0
        while last < len(nums):
            current += nums[last]
            counter +=1
            while counter - k > current:
                counter -= 1
                if nums[first] == 1:
                    current -= 1
                first += 1
            maxi = max(counter,maxi)  
            last += 1
        return maxi
