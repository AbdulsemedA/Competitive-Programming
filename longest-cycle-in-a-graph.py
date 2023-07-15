class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        memo = [0] * n
        maxi = -1

        def dfs(node, depth):
            nonlocal maxi

            if visited[node]:
                longest = depth - visited[node]

                memo[node] = max(memo[node], longest)
                maxi = max(maxi, longest)

                return longest

            visited[node] = depth

            if edges[node] != -1:
                longest = memo[edges[node]] or dfs(edges[node], depth + 1)
                memo[node] = max(memo[node], longest)

            visited[node] = False
            return memo[node]

        for i in range(n):
            if not visited[i]:
                dfs(i, 1)

        return maxi