class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = [item for item in s]
        
        for item in spaces:
            arr[item] = " " + arr[item]
            
        return ''.join(arr)
        