class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low + 1) // 2
        if (high - low + 1) % 2 and low % 2:
            odds += 1
        
        return odds
                
            
        