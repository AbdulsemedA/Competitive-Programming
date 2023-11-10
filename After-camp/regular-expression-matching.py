class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}

        def match(idx_s, idx_p):
            if (idx_s, idx_p) in memo:
                return memo[(idx_s, idx_p)]
        
            if idx_p == m:
                return idx_s == n
        
            found = idx_s < n and (p[idx_p] == s[idx_s] or p[idx_p] == '.')
        
            if idx_p + 1 < m and p[idx_p + 1] == '*':
                valid = match(idx_s, idx_p+2) or (found and match(idx_s + 1, idx_p))
            else:
                valid = found and match(idx_s + 1, idx_p + 1)
        
            memo[(idx_s, idx_p)] = valid
            return valid
    
        return match(0, 0)