class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_sum = sum(cardPoints)
        maxi = 0 
        cur_window = sum(cardPoints[:len(cardPoints) - k])
        maxi = total_sum - cur_window
        for i in range(k):
            cur_window = cur_window - cardPoints[i] + cardPoints[i + len(cardPoints) - k]
            points = total_sum - cur_window 
            maxi = max(points,maxi)
        return maxi
