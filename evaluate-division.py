class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for i, (A, B) in enumerate(equations):
            graph[A].append((B, values[i]))
            graph[B].append((A, 1 / values[i]))

        def dijkstra(graph, start, end):
            if start not in graph or end not in graph:
                return -1

            distances = {node: float('inf') for node in graph}
            distances[start] = 1
            heap = [(1, start)]

            while heap:
                dist, curr = heapq.heappop(heap)

                if curr == end:
                    return dist

                if dist > distances[curr]:
                    continue

                for neighbor, weight in graph[curr]:
                    distance = dist * weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))

            return -1

        results = []

        for start, end in queries:
            results.append(dijkstra(graph, start, end))

        return results