class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        S1 = defaultdict(int)
        S2 = defaultdict(int)
        l = r = 0

        for ele in s1: S1[ele] += 1
        
        while r < len(s2):
            while r - l >= len(s1):
                if S1 == S2: return True

                if S2[s2[l]] > 1:
                    S2[s2[l]] -= 1
                else:
                    del S2[s2[l]]
                
                l += 1

            S2[s2[r]] += 1
            r += 1

            if r == len(s2) and S1 == S2: return True