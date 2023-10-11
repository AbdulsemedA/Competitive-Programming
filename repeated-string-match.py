class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        i = 0
        n = len(b)

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

        LPS = KMP(b)
        curr = 0
        match = False
        
        while i < n:
            if not match and curr >= len(a):
                return -1

            if b[i] == a[curr % len(a)]:
                i += 1
                curr += 1
                match = True
            else:
                if match and curr >= 2 * len(a):
                    return -1
                
                if i:
                    i = LPS[i - 1]
                else:
                    curr += 1
        
        if i == n:
            return ceil(curr / len(a))
        return -1