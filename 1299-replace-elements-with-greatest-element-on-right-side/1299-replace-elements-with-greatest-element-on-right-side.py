class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        n = len(arr)
        
        for item in range(n - 1, -1, -1):
            temp = arr[item]
            arr[item] = maxi
            maxi = max(maxi,temp)
        
        return arr
            
        