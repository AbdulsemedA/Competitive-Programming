class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_words = {}
        n = len(p)
        
        res = []
        for i in p:
            p_words[i] = 1 + p_words.get(i, 0)
        
        checker = {}
        
        left = right = 0
        
        while right < len(s):
            checker[s[right]] = 1 + checker.get(s[right], 0)
            
            if right - left + 1 == n:
                if checker == p_words:
                    res.append(left)
                checker[s[left]] -= 1
                    
                if checker[s[left]] == 0:
                    del checker[s[left]]
                        
                left += 1
                    
            right += 1
                   
        return res
                    
            
            
            
        
        