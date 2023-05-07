class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pile = [-1 * i for i in piles]
        heapq.heapify(pile)
        
        for _ in range(k):
            curr = abs(heapq.heappop(pile))
            curr -= (curr // 2)
            heapq.heappush(pile, -curr)
        
        return abs(sum(pile))