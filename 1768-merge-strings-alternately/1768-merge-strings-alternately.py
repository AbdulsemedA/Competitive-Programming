class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_array = [char for char in word1]
        word2_array = [char for char in word2]
        
        output = ""
        index = 0
        minimum = min(len(word1),len(word2))
        
        while index < min(len(word1),len(word2)):
            output += word1[index] + word2[index]
            index += 1
            
        word1 = word1[minimum:]
        word2 = word2[minimum:]
        output += ''.join(word1) + ''.join(word2)
        
        return output
        
        