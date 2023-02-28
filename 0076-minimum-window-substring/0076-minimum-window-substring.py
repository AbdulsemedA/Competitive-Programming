class Solution:
    def minWindow(self, s: str, t: str) -> str:
        S_count = {}
        T_count = {}
        left = right = 0
        n, m = len(s), len(t)
        
        for i in t:
            T_count[i] = T_count.get(i, 0) + 1
        
        required = len(T_count)
        created = 0
        L, R = 0, n
        
        while right < n:
            curr = s[right]
            S_count[curr] = S_count.get(curr, 0) + 1
            
            if curr in T_count and S_count[curr] == T_count[curr]:
                created += 1
                
            while created == required and left <= right:
                if right - left + 1 < R - L + 1:
                    L, R = left, right
                    
                before = s[left]
                S_count[before] -= 1
                
                if before in T_count and S_count[before] < T_count[before]:
                    created -= 1
                
                left += 1

            right += 1

        return s[L:R + 1] if R != n else ""

        