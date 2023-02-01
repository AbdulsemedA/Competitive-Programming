class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        P1 = P2 = 0
        
        while P1 < len(word1) and P2 < len(word2):
            if word1[P1:] >= word2[P2:]:
                merge += word1[P1]
                P1 += 1
            else:
                merge += word2[P2]
                P2 += 1
        
        merge += ''.join(word1[P1:])
        merge += ''.join(word2[P2:])
            
        return merge
        