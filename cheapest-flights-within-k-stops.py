class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = {i: (float('inf'), float('inf')) for i in range(n)}
        distances[src] = (0, -1)
        graph = defaultdict(list)

        for frm, to, price in flights:
            graph[frm].append((to, price))
            
        heap = deque([(0, -1, src)])

        while heap:
            dist, count, node = heap.popleft()
            
            if count >= k: continue

            for neighbor, price in graph[node]:
                new_dist =  dist + price
                new_count = count + 1

                if new_dist < distances[neighbor][0]:
                    distances[neighbor] = (new_dist, new_count)
                    heap.append((new_dist, new_count , neighbor))

        return distances[dst][0] if distances[dst][1] <= k else -1