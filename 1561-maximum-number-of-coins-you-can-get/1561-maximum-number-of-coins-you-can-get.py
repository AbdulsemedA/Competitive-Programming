class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        bob = len(piles) // 3
        
        for k in range(bob,len(piles),2):
            result += piles[k] 
            
        return result
            
        