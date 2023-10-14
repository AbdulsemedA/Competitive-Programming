class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        large = [0] * n
        small = [0] * n
        total = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    large[i] += 1
                else:
                    small[i] += 1
        
        for i in range(n - 2):
            for j in range(i + 1, n):
                if rating[j] < rating[i]:
                    total += small[j]
                else:
                    total += large[j]
        
        return total