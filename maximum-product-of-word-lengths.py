class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0
        bits = []

        for i in range(len(words)):
            string = ["0"] * 26
            for x in range(len(words[i])):
                string[ord(words[i][x]) - ord("a")] = "1"
            bits.append(int(''.join(string), 2))
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bits[i] & bits[j] == 0:
                    maxi = max(maxi, len(words[i]) * len(words[j]))
        
        return maxi