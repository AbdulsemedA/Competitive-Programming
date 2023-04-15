class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if (xi - xj)**2 + (yi - yj)**2 <= (ri)**2:
                    graph[i].append(j)
                if (xi - xj)**2 + (yi - yj)**2 <= (rj)**2:
                    graph[j].append(i)
        
        def dfs(node, visited):
            visited[node] = True
            count = 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    count += dfs(neighbor, visited)
            return count
        
        maxi = 0

        for i in range(n):
            visited = [False] * n
            count = dfs(i, visited)
            maxi = max(maxi, count)
        
        return maxi