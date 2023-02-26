class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_S1 = {}
        freq_S2 = {}
        left = right = 0
        
        for item in s1:
            freq_S1[item] = 1 + freq_S1.get(item, 0)
        
        while right < len(s2):
            while right - left >= len(s1):
                if freq_S1 == freq_S2:
                    return True
                
                if freq_S2[s2[left]] > 1:
                    freq_S2[s2[left]] -= 1
                else:
                    del freq_S2[s2[left]]
                    
                left += 1
                
            freq_S2[s2[right]] = 1 + freq_S2.get(s2[right], 0)
            
            right += 1
        
        if freq_S1 == freq_S2:
            return True
        
        return False
            
            