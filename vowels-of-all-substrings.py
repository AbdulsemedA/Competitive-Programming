class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = set(['a','e', 'i', 'o', 'u'])
        ans = 0

        for idx in range(n):
            if word[idx] in vowels:
                ans += (n - idx) * (idx + 1)
        
        return ans