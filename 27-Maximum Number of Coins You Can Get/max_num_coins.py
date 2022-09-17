class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        bob = int(len(piles)/3)
        piles.sort()
        piles = piles[bob:len(piles)]
        for k in range(len(piles)):
            if k % 2 == 0:
                result+= piles[k]    
        return result
