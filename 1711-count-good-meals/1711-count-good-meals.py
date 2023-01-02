class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        modulus = 10**9 + 7
        ans = 0
        hmap = {}
        
        for item in deliciousness:
            hmap[item] = 1 + hmap.get(item,0)
            
        for key, value in hmap.items():
            for item in range(22):
                diff = (2 ** item) - key
                if diff in hmap:
                    if diff == key:
                        ans += int(((value - 1) * value) / 2)
                    else:
                        ans += hmap[diff] * value
                        
            hmap[key] = 0
            
        return ans % modulus
        
        
        
        