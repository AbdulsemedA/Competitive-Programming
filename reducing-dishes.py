class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        neg, maxi = [], 0

        for i in range(n):
            if satisfaction[i] >= 0: break
            neg.append(satisfaction[i])
        
        pos = satisfaction[i:]
        total = sum(pos)
        sums = sum([i * (idx + 1) for idx, i in enumerate(pos)])
        maxi = max(maxi, sums)
        
        for i in range(len(neg) - 1, -1, -1):
            maxi = max(maxi, sums + total + neg[i])
            sums += total + neg[i]
            total += neg[i]
            
        return maxi