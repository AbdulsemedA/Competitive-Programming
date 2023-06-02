class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = defaultdict(int)
        n = len(questions)

        def dp(idx):
            if idx >= n: return 0
            if idx == n - 1: return questions[idx][0]
            
            if idx in memo: return memo[idx]
            val, itr = questions[idx]

            take = val + dp(idx + itr + 1)
            skip = dp(idx + 1)
            memo[idx] = max(take, skip)

            return memo[idx]
        
        return dp(0)