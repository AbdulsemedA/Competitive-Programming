class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = [1] * k
        
        for i in range(1, k):
            powers[i] = powers[i-1] * power
        
        def hasher(word):
            ans = curr = 0

            for ch in word:
                ans += powers[curr] * (ord(ch) - 96)
                curr += 1
            
            return ans

        base = hasher(s[:k])
        if base % modulo == hashValue: return s[:k]

        for i in range(k, len(s)):
            base -= (ord(s[i - k]) - 96)
            base //= power
            base += (ord(s[i]) - 96) * powers[k - 1]
            
            if base % modulo == hashValue:
                return s[i - (k - 1):i+1]