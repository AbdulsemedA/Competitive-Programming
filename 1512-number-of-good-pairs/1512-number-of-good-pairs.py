from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = defaultdict(list)
        pairs = 0
        
        for index,item in enumerate(nums):
            if item in hmap:
                hmap[item].append(index)
                continue
            hmap[item].append(index)
        
        for item in hmap:
            current_size = self.pairCount(len(hmap[item]))
            pairs += current_size
        
        return pairs
            
    def pairCount(self, size) -> int:
        return ((size * (size + 1)) // 2) - size
        
        