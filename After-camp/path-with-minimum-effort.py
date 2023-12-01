import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        direction = [(-1,0), (1,0), (0, -1), (0,1)]
        
        def inbound(x ,y):
            return 0 <= x < m and 0 <= y < n

        distances = {}

        for i in range(m):
            for j in range(n):
                distances[(i,j)] = float('inf')

        distances[(0, 0)] = 0
        visited = set()
        heap = [(0, (0, 0))]

        while heap:
            dist, node = heapq.heappop(heap)
            
            if (dist,node) in visited:
                continue
            visited.add((dist,node))
            
            for u, v in direction:
                x, y = node[0] + u, node[1] + v
                
                if inbound(x, y):
                    distance = max(dist, abs(heights[x][y] - heights[node[0]][node[1]]))

                    if distance < distances[(x,y)]:
                        distances[(x,y)] = distance
                        heapq.heappush(heap, (distance, (x,y)))
                
        return distances[(m-1, n-1)]