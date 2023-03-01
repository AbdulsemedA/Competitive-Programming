class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n, total = len(nums), 0
        prefix = [i % 2 for i in nums]
        left = right = prev = 0
                
        for i in range(1,n):
            prefix[i] += prefix[i-1]
            
        while right < n:
            curr = prefix[right]
            count = 0
            
            if curr - prev == k:
                count = 1
                while left < right and prefix[left] - prev == 0:
                    count += 1
                    left += 1
                right += 1
                total += count
                
                while right < n and prefix[right] == curr:
                    total += count
                    right += 1
                
                left += 1
                prev += 1
                continue
                
            right += 1
        
        return total