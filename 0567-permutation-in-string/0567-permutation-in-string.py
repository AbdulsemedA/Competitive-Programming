class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        
        for i in range(m-n+1):
            if sorted(s2[i:n+i]) == sorted(s1):
                return True
        
        return False
            
        