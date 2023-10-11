class Solution:
    def longestPrefix(self, s: str) -> str:
        def KMP(p):
            m = len(p)
            prevLPS, i = 0, 1
            LPS = [0 for _ in range(m)]
            
            while i < m:
                if p[prevLPS] == p[i]:
                    LPS[i] = prevLPS + 1
                    prevLPS += 1
                    i += 1
                else:
                    if prevLPS == 0:
                        i += 1
                    else:
                        prevLPS = LPS[prevLPS - 1]
                
            return LPS
        
        LPS = KMP(s)
        print(LPS)
        if not LPS[-1]:
            return ''
        return s[len(s) - 1 - LPS[-1] + 1:]