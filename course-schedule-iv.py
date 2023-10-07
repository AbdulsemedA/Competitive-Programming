class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i, j in prerequisites:
            dist[i][j] = 1

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = []

        for u, v in queries:
            if dist[u][v] == float('inf'):
                ans.append(False)
            else:
                ans.append(True)
        
        return ans