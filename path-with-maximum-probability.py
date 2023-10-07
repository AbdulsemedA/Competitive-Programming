import heapq
import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        distances = {i: float('-inf') for i in range(n)}
        distances[start_node] = 0
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))

        visited = set()
        heap = [(-1, start_node)]

        while heap:
            dist, node = heapq.heappop(heap)
            dist *= -1

            if node in visited:
                continue

            visited.add(node)

            for neighbor, prob in graph[node]:
                new_dist = dist * prob

                if new_dist > distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (-new_dist, neighbor))

        return distances[end_node] if distances[end_node] != float('-inf') else 0