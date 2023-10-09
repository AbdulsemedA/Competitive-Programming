class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = ceil(total / 2)
        memo = {}
        n = len(stones)

        def find(i, curr):
            if curr >= target or i == n:
                return abs(curr - (total - curr))
            
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            memo[(i, curr)] = min(find(i + 1, curr), find(i + 1, curr + stones[i]))

            return memo[(i, curr)]
        
        return find(0, 0)