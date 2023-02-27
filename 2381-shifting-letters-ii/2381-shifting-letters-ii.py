class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n, curr = len(s), 0
        prefix = [0] * (n+1)
        
        for left, right, path in shifts:
            if path:
                prefix[left] += 1
                prefix[right + 1] -= 1
            else:
                prefix[left] -= 1
                prefix[right + 1] += 1
                
        prefix.pop()
        
        for i in range(1, n):
            curr = prefix[i-1]
            prefix[i] += curr
            
        for i in range(len(prefix)):
            new = ord(s[i]) + prefix[i]
            
            if new < 97:
                while new < 97:
                    new += 26
            elif new > 122:
                while new > 122:
                    new -= 26
            
            prefix[i] = chr(new)
        
        return ''.join(prefix)
        