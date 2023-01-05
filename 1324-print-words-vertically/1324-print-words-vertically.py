class Solution:
    def printVertically(self, s: str) -> List[str]:
        array = s.split(" ")
        diction = {}
        size = len(array)
        result = []
        
        for item in range(size):
            diction[item] = len(array[item])
            
        maxi = max(diction.values())
        
        for item in range(size):
            array[item] += (maxi - len(array[item])) * " "
            array[item] = [ch for ch in array[item]]
            
        for outer in range(maxi):
            result.append("")
            
            for inner in range(size):
                result[-1] += array[inner][outer]
            
        return [item.rstrip() for item in result]
            
            
        
            
            
            
        