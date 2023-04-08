class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        vals = count.values()

        if min(vals) < 2:
            return False
            
        gcd_vals = gcd(*vals)
        return gcd_vals >= 2