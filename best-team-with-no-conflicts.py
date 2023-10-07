class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ages, scores = zip(*sorted(zip(ages, scores)))
        dp = list(scores).copy()

        for i in range(1, n):
            for j in range(i):
                if (scores[i] >= scores[j] and dp[i] < dp[j] + scores[i]):
                    dp[i] = dp[j] + scores[i]

        return max(dp)