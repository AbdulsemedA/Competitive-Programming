class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = {}
        maxi = 1
        left = right = 0
        
        while right < len(s):
            if s[right] in word:
                maxi = max(maxi, right - left)
                if word[s[right]] >= left:
                    left = word[s[right]] + 1
                    
            word[s[right]] = right     
            right += 1
        
        maxi = max(maxi, right - left)
        
        if s:
            return maxi
        return 0
            
            
        
        