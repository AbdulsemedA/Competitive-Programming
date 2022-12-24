class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictionary_T = {}
        
        for char in t:
            dictionary_T[char] = 1 + dictionary_T.get(char,0)
            
        for item in dictionary_T:
            if dictionary_T[item] > s.count(item):
                return item
        