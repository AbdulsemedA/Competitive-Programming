class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[0 for i in range(n)] for i in range(n)]
        maxi = 0

        for ele in roads:
            src, des = ele
            graph[src][des] = 1
            graph[des][src] = 1
        
        row_sum = [sum(i) for i in graph]
        
        for i in range(n):
            for j in range(i + 1, n):
                total = row_sum[i] + row_sum[j]
                if graph[i][j] == graph[j][i] == 1:
                    total -= 1
                maxi = max(maxi, total)
        
        return maxi