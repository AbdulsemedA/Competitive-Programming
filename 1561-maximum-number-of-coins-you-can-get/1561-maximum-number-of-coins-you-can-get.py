class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0 
        piles.sort()
        
        for k in range(len(piles) // 3,len(piles),2):
            result+= piles[k] 
            
        return result
            
        