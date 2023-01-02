class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        total = ''
        current = 0
        
        for item in spaces:
            total += s[current:item] + " "
            current = item
            
        total += s[current:]
            
        return total
        