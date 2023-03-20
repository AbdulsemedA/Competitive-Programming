class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr, size):
            if size == k:
                result.append(curr)
                return
                
            for i in range(start, n + 1):
                backtrack(i + 1, curr + [i], size + 1)

        backtrack(1, [], 0)
        return result