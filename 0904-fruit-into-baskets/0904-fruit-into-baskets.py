class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi, n = 0, len(fruits)
        left = right = 0
        count = {}
        
        while right < n:
            if fruits[right] not in count and len(count) == 2:
                maxi = max(right - left, maxi)
                before = fruits[left]
            
                while before in count and count[before] > 0 and len(count) > 1:
                    count[fruits[left]] -= 1
                    
                    if count[fruits[left]] == 0:
                        del count[fruits[left]]
                        
                    left += 1
                    
            count[fruits[right]] = 1 + count.get(fruits[right], 0)
            right += 1
            
            if right == len(fruits) and len(count) < 3:
                maxi = max(right - left, maxi)
                
        return maxi
        
        