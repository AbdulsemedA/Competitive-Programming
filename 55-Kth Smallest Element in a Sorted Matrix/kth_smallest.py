class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        total = []
        for i in matrix:
            total += i
        total.sort()
        total = total[k-1:]
        return min(total)
